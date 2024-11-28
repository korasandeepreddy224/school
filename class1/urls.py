
from class1.views import *
from django.urls import path


urlpatterns = [
    path('school/',school,name='school'),
    path('school2/',school2,name='school2'),
]