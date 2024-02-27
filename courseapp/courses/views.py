from django.http import HttpResponse
from django.shortcuts import render

def courses(request):
    return HttpResponse('Course List')

def details(request):
    return HttpResponse('Course Details Page')

def programming(request):
    return HttpResponse('Programming Course List')

def mobileapplications(request):
    return HttpResponse('Mobile Applications Course List')