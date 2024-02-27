from django.http import HttpResponse
from django.shortcuts import render

def courses(request):
    return HttpResponse('Course List')

def details(request, course_name):
    return HttpResponse(f"{course_name} detail page")

def getCoursesByCategoryName(request, category_name):
    text = ''
    if(category_name == "programming"):
        text = "List of courses in the Programming Category"
    elif(category_name == "web-development"):
        text = "List of courses in the Web Development Category"
    else:
        text = "False Category Selection"
        
    return HttpResponse(text)

def getCoursesByCategoryId(request, category_id):
    return HttpResponse(category_id)