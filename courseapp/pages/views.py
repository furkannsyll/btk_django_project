from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Homepage')

def contact(request):
    return HttpResponse('Contact Page')

def about(request):
    return HttpResponse('About Us')