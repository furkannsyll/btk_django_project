from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('Homepage')

def courses(request):
    return HttpResponse('Course List')