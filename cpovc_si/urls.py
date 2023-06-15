from django.urls import path, re_path
from . import views

# This should contain urls related to si ONLY

urlpatterns = [
    path('', views.si_home, name='Statutory Institution'),
    path(
    'new/<uuid:case_id>/', views.new_statutory_institution,
    name='new_si_institution'),
    path(
    'view/<uuid:care_id>/', views.view_statutory_institution,
    name='view_si_institution'),
    path('commonforms/admission/', views.admission, name='admission'),
    path('commonforms/biodata/', views.biodata, name='biodata'),
    path('commonforms/exit/', views.exit, name='exit'),
    path('create_person/', views.create_person, name='create_person'),
    # path('commonforms/pre_admission/', views.preadmission, name='preadmission'),
    # path('commonforms/pre_exit/', views.pre_exit, name='preadmission'),
    # path('commonforms/stay/', views.stay, name='preadmission'),
]
