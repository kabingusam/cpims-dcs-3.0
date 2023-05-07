from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import RadioSelect

from cpovc_main.functions import get_list, get_org_units_list
from cpovc_registry.functions import (
    get_geo_list, get_all_geo_list, get_all_location_list,
    get_all_sublocation_list)
from cpovc_registry.models import RegOrgUnit
# from .functions import get_questions
# Added for CTiP
from cpovc_main.country import OCOUNTRIES

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

