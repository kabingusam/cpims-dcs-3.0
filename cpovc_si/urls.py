from django.urls import path, re_path
from . import views

# This should contain urls related to si ONLY

urlpatterns = [
    path('test/', views.test, name='si'),
]