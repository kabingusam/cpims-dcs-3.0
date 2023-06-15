from django.shortcuts import render
from cpovc_si.forms import AFCForm1A, RehabAdmission
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Person
from django.shortcuts import render
from django.http import HttpResponseRedirect

from cpovc_forms.forms import OVCSearchForm
from cpovc_forms.functions import get_person_ids
from cpovc_registry.models import (RegPerson)
from cpovc_forms.models import OVCCaseRecord,OVCCaseCategory
from .models import SIMain
from .forms import StatutorySearchForm
from cpovc_registry.functions import names_from_ids
from cpovc_auth.models import AppUser
from cpovc_registry.models import (RegPersonsTypes)
from cpovc_auth.decorators import is_allowed_groups
from cpovc_main.functions import (
    get_list_of_org_units, get_dict, convert_date, get_list_of_persons)
from django.contrib.auth.decorators import login_required
from cpovc_afc.forms import AltCareForm
from django.urls import reverse
from .functions import (handle_alt_care,get_form_info)
from .settings import FMS, CTS

from cpovc_afc.models import AFCMain, AFCEvents, AFCForms
from django.db.models import Count

# Create your views here.
def home(request):
    return render(request, 'si/home.html')

@login_required
def si_home(request):
    '''
    Some default page for forms home page
    '''
    try:
        form = OVCSearchForm(data=request.GET)
        # form = SearchForm(data=request.POST)
        # person_type = 'TBVC'
        afc_ids, case_ids = {}, {}
        search_string = request.GET.get('search_name')
        pids = get_person_ids(request, search_string)
        cases = RegPerson.objects.filter(is_void=False, id__in=pids)
        # Get case record sheet details
        crss = OVCCaseRecord.objects.filter(is_void=False, person_id__in=pids)
        for crs in crss:
            case_ids[crs.person_id] = {'clv': 1, 'cid': crs.case_id}
        # Check if there is a filled AFC Form
        # afcs = AFCMain.objects.filter(is_void=False, person_id__in=pids)
        # for afc in afcs:
            # afc_ids[afc.person_id] = {'cid': afc.care_id,
                                    #   'clv': 2, 'cdt': afc.case_date}
        for case in cases:
            pid = case.id
            cid = afc_ids[pid]['cid'] if pid in afc_ids else 'N/A'
            cdt = afc_ids[pid]['cdt'] if pid in afc_ids else 'N/A'
            clvf = case_ids[pid]['clv'] if pid in case_ids else 0
            crs_id = case_ids[pid]['cid'] if pid in case_ids else None
            clv = afc_ids[pid]['clv'] if pid in afc_ids else clvf
            setattr(case, 'case_t', str(cid))
            setattr(case, 'care_id', cid)
            setattr(case, 'case_date', cdt)
            setattr(case, 'case_level', clv)
            setattr(case, 'case_id', crs_id)
        return render(request, 'si/home.html',
                      {'status': 200, 'cases': cases, 'form': form})
    except Exception as e:
        raise e

@login_required
def new_statutory_institution(request, case_id):
    '''
    New Statutory Institution main page
    '''
    try:
        cid = 'XX'
        form = AltCareForm(initial={'person_type': 'TBVC'})
        check_fields = ['sex_id', 'case_category_id']
        vals = get_dict(field_name=check_fields)
        selected_value = 'one'
        # Case Categories
        case = OVCCaseRecord.objects.get(case_id=case_id)
        categories = OVCCaseCategory.objects.filter(case_id_id=case_id)
        care = AFCMain.objects.filter(
            is_void=False, case_id=case_id, case_status__isnull=True)
        if care:
            my_care = care.first()
            care_id = my_care.care_id
            msg = 'Child already enrolled to Statutory Institution '
            msg += 'and case management is ongoing.'
            messages.add_message(request, messages.ERROR, msg)
            cid = str(my_care.care_type)[2:]
            url = reverse(view_statutory_institution, kwargs={'care_id': care_id})
            return HttpResponseRedirect(url)

        if request.method == 'POST':
            selected_value = request.POST.get('search_institution')
            afc_params = {}
            person_id = case.person_id
            afc_params['case_id'] = case_id
            afc_params['person_id'] = person_id
            afc_params['case_cid'] = cid
            care_id = handle_alt_care(request, 0, afc_params)
            #url = reverse(view_statutory_institution, kwargs={'care_id': care_id})
            return render(request, 'si/new_statutory_institution.html',
                      {'status': 200, 'case_id': case_id, 'vals': vals,
                       'categories': categories, 'case': case,
                       'form': form, 'care': care, 'nid': case_id,
                       'cid': cid,'selected_value':selected_value})
        return render(request, 'si/new_statutory_institution.html',
                      {'status': 200, 'case_id': case_id, 'vals': vals,
                       'categories': categories, 'case': case,
                       'form': form, 'care': care, 'nid': case_id,
                       'cid': cid,'selected_value':selected_value})
    except Exception as e:
        raise e

def search_institution(request):
    if request.method == 'POST':
        selected_value = request.POST.get('search_institution')

    return render(request, 'si/commonforms/admission.html', {'form': form})

@login_required
def view_statutory_institution(request, care_id):
    '''
    View Statutory Institution main page
    '''
    try:
        case = AFCMain.objects.get(is_void=False, care_id=care_id)
        if case.care_type:
            cid = str(case.care_type)[2:]
        else:
            cid = 'XX'
        cname = CTS[cid] if cid in CTS else 'Missing Assessments'
        check_fields = ['sex_id', 'case_category_id',
                        'alternative_family_care_type_id',
                        'care_admission_reason_id']
        vals = get_dict(field_name=check_fields)
        # Events
        events = (AFCEvents.objects
                  .filter(care_id=care_id)
                  .values('form_id')
                  .annotate(dcount=Count('form_id'))
                  .order_by()
                  )
        # Common data
        fdatas = get_form_info(request, case.pk, case.person_id, False)
        forms, fforms= {}, []
        for event in events:
            forms[str(event['form_id'])] = event['dcount']
            fforms.append(str(event['form_id']))
        print('forms', forms)
        return render(request, 'afc/view_alternative_care.html',
                      {'status': 200, 'case': case, 'vals': vals,
                       'cid': cid, 'care_name': cname, 'events': forms,
                       'fdatas': fdatas})
    except Exception as e:
        raise e
    
def admission(request):
    if request.method == 'POST':
        form = RehabAdmission(request.POST)
        if form.is_valid():
        # Save the form data
            form.save()
        # Set success message
            messages.success(request, 'Form submitted successfully')
        # Redirect to success page
            return redirect('success_page')
    else:
        form = AFCForm1A()
    return render(request, 'si/commonforms/admission.html', {'form': form})

def biodata(request):
    if request.method == 'POST':
        form = AFCForm1A(request.POST)
        if form.is_valid():
            # Save the form data
            form.save()
            # Set success message
            messages.success(request, 'Form submitted successfully')
            # Redirect to success page
            return redirect('success_page')
    else:
        form = AFCForm1A()
    return render(request, 'si/commonforms/biodata.html', {'form': form})

def exit(request):
    if request.method == 'POST':
        form = AFCForm1A(request.POST)
        if form.is_valid():
            # Save the form data
            form.save()
            # Set success message
            messages.success(request, 'Form submitted successfully')
            # Redirect to success page
            return redirect('success_page')
    else:
        form = AFCForm1A()
    return render(request, 'si/commonforms/exit.html', {'form': form})

def create_person(request):
    if request.method == 'POST':
        form = Person(request.POST)
        if form.is_valid():
            person = Person(
                first_name=form.cleaned_data['first_name'],
                other_names=form.cleaned_data['other_names'],
                surname=form.cleaned_data['surname'],
                nickname=form.cleaned_data['nickname'],
                sex=form.cleaned_data['sex'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                county=form.cleaned_data['county'],
                sub_county=form.cleaned_data['sub_county'],
                ward=form.cleaned_data['ward'],
                location=form.cleaned_data['location'],
                sub_location=form.cleaned_data['sub_location'],
                village=form.cleaned_data['village'],
            )
            print(f'Saving person: {person.__dict__}')
            person.save()
            print(f'Save result: {person.pk}')
            return HttpResponseRedirect('/success/')
    else:
        form = Person()
    return render(request, 'si/si.html', {'form': form})
