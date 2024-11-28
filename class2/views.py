from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def school(request):
    return HttpResponse('class2')


def school2(request):
    return HttpResponse('class2 childes ')
