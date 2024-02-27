from django.http import HttpResponse
from django.shortcuts import render

def courses(request):
    return HttpResponse('Course List')

def details(request):
    return HttpResponse('Course Details Page')

def getCoursesByCategory(request, category):
    text = ''
    if(category == "programming"):
        text = "List of courses in the Programming Category"
    elif(category == "web-development"):
        text = "List of courses in the Web Development Category"
    else:
        text = "False Category Selection"
        
    return HttpResponse(text)