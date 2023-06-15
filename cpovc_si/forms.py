from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import RadioSelect

from cpovc_registry.functions import (
    get_geo_list, get_all_geo_list, get_all_location_list,
    get_all_sublocation_list)
from cpovc_registry.models import RegOrgUnit
# from .functions import get_questions
# Added for CTiP
from cpovc_main.functions import get_list, get_lists
immunization_list = get_list('immunization_status_id', 'Please Select')

person_type_list = get_list('person_type_id', 'Please Select Type')
school_level_list = get_list('school_level_id', 'Please Select Level')
admission_list = get_list('school_type_id', 'Please Select one')
disability_list = get_list('disability_type_id', 'Please Select one')
severity_list = get_list('severity_level_id', 'Please Select one')
admission_type_list = get_list('admission_type_id', 'Please Select')
admission_reason_list = get_list('care_admission_reason_id')
domain_list = get_list('afc_domain_id', 'Please Select')
list_sex_id = get_list('sex_id')
consent_forms_list = get_list('consent_forms', 'Please Select')
# new listings
list_other_adms = get_list('other_form_admission', 'Please Select')
list_other_vulnerability = get_list(
    'vulnerability_at_admission', 'Please Select')
list_relationship = get_list('relationship_type_id', 'Please Select')
list_education_perf = get_list('education_performance')
list_marriage_type = get_list('parents_marriage_type', 'Please Select')
list_items_count = get_list('items_count_id', 'Please Select')
list_special_support = get_list('special_support')
list_community_services = get_list('community_services')
list_school_category = get_list('school_category_id', 'Please Select')
list_range_level = get_list('attachment_level', 'Please Select')
list_range_level_rdo = get_lists(['attachment_level', 'na_option'])
list_child_exhibits = get_list('child_exhibits')
list_income_range = get_list('income_range', 'Please Select')
list_employment_type = get_list('employment_type', 'Please Select')
list_closure_reasons = get_list('case_closure_reasons', 'Please Select')
list_case_transfer_ids = get_list('case_transfer_ids', 'Please Select')
list_satisfied_level = get_list('satisfied_level_ids')
list_feeling_level = get_list('feeling_level_ids')
list_referral_reasons = get_list('referral_reasons_ids', 'Please Select')
list_referral_documents = get_list('referral_documents_ids')
list_case_plan_responsible = get_list('case_plan_responsible', 'Please Select')

disability_actions = get_list('disability_actions')
list_family_types = get_list('family_type_id', 'Please Select')

YESNO_UN_CHOICES = get_list('yesno_una')
list_disability_assessment = get_list('disability_assessment_id')
list_disability_handling = get_list('disability_handling_id')
list_attachment_assessment = get_list(
    'attachment_assessment_id', 'Please select')


YESNO_CHOICES = get_list('yesno_id')
YESNO_UK_CHOICES = get_lists(['yesno_id', 'uk_option'])
care_option_list = get_list(
    'alternative_family_care_type_id', 'Please Select Care')

disability_degree = (('0', '0'), ('1', '1'), ('2', '2'),
                     ('3', '3'), ('4', '4'), )

YESNONA_choices = get_list('yesno_na')
list_sex_other_id = get_list('sex_id', 'Please Select')
list_ratings = get_list('ratings_id')
list_frequency = get_lists(['period_frequency_id', 'na_option'])

# joseph implimentation
psearch_criteria_list = get_list('psearch_criteria_type_id', 'Select Criteria')

class RadioCustomRenderer(RadioSelect):
    """Custom radio button renderer class."""

    def render(self):
        """Renderer override method."""
        pass

class StatutorySearchForm(forms.Form):
    """Search registry form."""

    person_type = forms.ChoiceField(
        choices=person_type_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'person_type',
                   'data-parsley-required': 'true'}))

    search_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': _('Search . . .'),
                   'class': 'form-control',
                   'id': 'search_name',
                   'data-parsley-group': 'primary',
                   'data-parsley-required': 'true'}))

    search_criteria = forms.ChoiceField(
        choices=psearch_criteria_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'search_criteria',
                   'data-parsley-required': 'true'}))

    person_deceased = forms.CharField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={'id': 'person_deceased'}))

 #joseph implimentation   
class RehabAdmission(forms.Form):
    """AFC Form 1A."""
    SEX_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
        ('O', _('Other')),
    )

    date_of_birth = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    child_name = forms.CharField(
        max_length=50,
        required=True,
        label=_("First Name"),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': _('This field is required.')},
        help_text=_("Enter your  name.")
    )

    mother_name = forms.CharField(
        max_length=50,
        required=True,
        label=_("Other Names"),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': _('This field is required.')},
        help_text=_("Enter your mother names.")
    )
    mother_address = forms.CharField(
        max_length=50,
        required=False,
        label=_("Other Names"),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': _('This field is required.')},
        help_text=_("Enter your mother address.")
    )
    mother_telephone = forms.CharField(
        max_length=50,
        required=True,
        label=_("Other Names"),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': _('This field is required.')},
        help_text=_("Enter your mother names.")
    )
    mother_is_alive = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={'id': 'has_bcert',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A1_rdo_error"}))

    father_name = forms.CharField(
        max_length=50,
        required=False,
        label=_("Nickname or given name"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    father_address = forms.CharField(
        max_length=50,
        required=False,
        label=_("Nickname or given name"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    father_telephone = forms.CharField(
        max_length=50,
        required=False,
        label=_("Nickname or given name"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    father_is_alive = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={'id': 'has_bcert',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A1_rdo_error"}))


    nickname = forms.CharField(
        max_length=50,
        required=False,
        label=_("Nickname or given name"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        required=True,
        label=_("Sex"),
        widget=forms.Select(attrs={'class': 'form-control'}),
        error_messages={'required': _('This field is required.')},
        help_text=_("Select your sex.")
    )

    age = forms.DateField(
        required=False,
    )

class DocumentsManager(forms.Form):
    document_type = forms.ChoiceField(
        # choices=document_type_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'document_type',
                   'data-parsley-required': 'true'}))

    document_description = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _('Document Description'),
               'class': 'form-control',
               'id': 'document_description',
               'data-parsley-required': 'true'}))

    search_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _('Enter Child Name(s)'),
               'class': 'form-control',
               'id': 'search_name',
               'data-parsley-required': 'true'}))

    file_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': _('File Name'),
               'class': 'form-control',
               'readonly': 'true',
               'id': 'file_name'}))

    search_criteria = forms.ChoiceField(
        # choices=psearch_criteria_list,
        initial='0',
        required=True,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'search_criteria',
                   'data-parsley-required': 'true'}))

    person = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'id': 'person',
               'type': 'hidden',
               'data-parsley-required': "true",
               'data-parsley-group': 'group0'
               }))

class AFCForm1A(forms.Form):
    """AFC Form 1A."""
    SEX_CHOICES = (
        ('M', _('Male')),
        ('F', _('Female')),
        ('O', _('Other')),
    )

    RELIGION_CHOICES = [
        ('Christian', 'Christian'),
        ('Muslim', 'Muslim'),
        ('Hindu', 'Hindu'),
    ]
    YES_CHOICE = [
        ('Yes', 'Yes'),
    ]

    COUNTY_CHOICES = (
    ('county1', 'County 1'),
    ('county2', 'County 2'),
    ('county3', 'County 3'),
    # Add more counties here
    )
    
    religion = forms.MultipleChoiceField(
        choices=RELIGION_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'square-button'})
    )
    yes_choice = forms.MultipleChoiceField(
        choices=YES_CHOICE,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'square-button'})
    )

    event_date = forms.DateField(widget=forms.TextInput(
        attrs={'placeholder': _('Date'),
               'class': 'form-control',
               'id': 'event_date',
               'data-parsley-required': "true"
               }))

    first_name = forms.CharField(
        max_length=50,
        required=True,
        label=_("First Name"),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': _('This field is required.')},
        help_text=_("Enter your first name.")
    )

    other_names = forms.CharField(
        max_length=50,
        required=True,
        label=_("Other Names"),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': _('This field is required.')},
        help_text=_("Enter your other names.")
    )

    surname = forms.CharField(
        max_length=50,
        required=True,
        label=_("Surname"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    nickname = forms.CharField(
        max_length=50,
        required=False,
        label=_("Nickname or given name"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        required=True,
        label=_("Sex"),
        widget=forms.Select(attrs={'class': 'form-control'}),
        error_messages={'required': _('This field is required.')},
        help_text=_("Select your sex.")
    )

    date_of_birth = forms.DateField(
        required=True,
        label=_("DOB"),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': _('This field is required.')},
        help_text=_("Enter your date of birth.")
    )

    county_of_birth = forms.ChoiceField(
        choices=COUNTY_CHOICES,
        required=True,
        label=_("Place of Birth: County"),
        widget=forms.Select(attrs={'class': 'form-control'}),
        error_messages={'required': _('This field is required.')},
        help_text=_("Select your county of birth.")
    )

    sub_county_of_birth = forms.CharField(
        max_length=50,
        required=True,
        label=_("Sub County"),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': _('This field is required.')},
        help_text=_("Enter your sub county of birth.")
    )

    location = forms.CharField(
        max_length=50,
        required=False,
        label=_("loaction"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    ward_of_birth = forms.CharField(
        max_length=50,
        required=True,
        label=_("Ward"),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': _('This field is required.')},
        help_text=_("Enter your ward of birth.")
    )

    sub_location = forms.CharField(
        max_length=50,
        required=False,
        label=_("Sub Location"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    village = forms.CharField(
        max_length=50,
        required=False,
        label=_("Village"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    available = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={'id': 'has_bcert',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A1_rdo_error",
                   'class': 'square-button'}))


    qf1A1_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={'id': 'has_bcert',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A1_rdo_error"}))

    qf1A2 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A2',
               'data-parsley-required': "false"}))

    qf1A3 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A3',
               'data-parsley-required': "false"}))

    qf1A4 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A4',
               'data-parsley-required': "false"}))

    qf1A5 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A5',
               'data-parsley-required': "false"}))

    qf1A6 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A6',
               'data-parsley-required': "false"}))

    qf1A7 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A7',
               'data-parsley-required': "false"}))

    qf1A8 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A8',
               'data-parsley-required': "false"}))

    qf1A10_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={'id': 'has_disability',
                   'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A2_rdo_error"}))

    qf1A11_sdd = forms.ChoiceField(
        choices=disability_list,
        initial='0',
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'disability_type'}))

    qf1A12_sdd = forms.ChoiceField(
        choices=severity_list,
        initial='0',
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'disability_severity'}))

    qf1A13 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control', 'id': 'qf1A13',
               'data-parsley-required': "false"}))

    qf1A14_sdd = forms.ChoiceField(
        choices=list_other_adms,
        initial='0',
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   'id': 'qf1A14_sdd'}))

    qf1A15_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A15_rdo_error"}))

    qf1A16 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A17 = forms.DateField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control event_date',
               'data-parsley-required': "false"}))

    qf1A18 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A19 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A20_sdd = forms.ChoiceField(
        choices=list_other_vulnerability,
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control'}))

    qf1A21 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A21A_sdd = forms.ChoiceField(
        choices=list_relationship,
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control'}))

    qf1A22_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A22_rdo_error"}))

    qf1A23_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=True,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A23_rdo_error"}))

    qf1A24_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=True,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A24_rdo_error"}))

    qf1A25_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'false',
                   'data-parsley-errors-container': "#qf1A25_rdo_error"}))

    qf1A25A = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A25B = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A26_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'false',
                   'data-parsley-errors-container': "#qf1A26_rdo_error"}))

    qf1A27_rdo = forms.ChoiceField(
        choices=YESNO_CHOICES,
        required=False,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'false',
                   'data-parsley-errors-container': "#qf1A27_rdo_error"}))

    qf1A27A = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': _(''),
               'class': 'form-control',
               'data-parsley-required': "false"}))

    qf1A28_rdo = forms.ChoiceField(
        choices=YESNONA_choices,
        required=True,
        widget=forms.RadioSelect(
            # renderer=RadioCustomRenderer,
            attrs={'data-parsley-required': 'true',
                   'data-parsley-errors-container': "#qf1A28_rdo_error"}))
