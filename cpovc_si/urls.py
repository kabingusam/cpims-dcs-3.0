from django.urls import path, re_path
from . import views

# This should contain urls related to si ONLY

urlpatterns = [
    path('test/', views.test, name='si'),
    path('commonforms/admission/', views.admission, name='admission'),
    path('commonforms/biodata/', views.biodata, name='biodata'),
    # path('commonforms/pre_admission/', views.preadmission, name='preadmission'),
    # path('commonforms/pre_exit/', views.pre_exit, name='preadmission'),
    # path('commonforms/stay/', views.stay, name='preadmission'),
]