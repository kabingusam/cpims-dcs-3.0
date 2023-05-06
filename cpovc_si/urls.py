from django.urls import path, re_path
from . import views


urlpatterns = [

     path('si/', views.test, name='test'),
     path('commonforms/admission/', views.admission, name='admission')

]