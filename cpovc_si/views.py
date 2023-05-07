from django.shortcuts import render
from cpovc_si.forms import AFCForm1A, RehabAdmission
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Person
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person

# Create your views here.
def test(request):
    return render(request, 'si/si.html')

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
