from datetime import date, datetime
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Course, Category

data = {
    "programming":"Courses in the Programming Category",
    "web-development":"Courses in the Web Development Category",
    "mobile":"Courses in the Mobile Category"
}

db = {
    "courses": [
     {
        "title":"Javascript Course",
        "description":"Javascript Course Description",
        "imageUrl":"1.jpg",
        "slug":"javascript-course",
        "date": datetime.now(),
        "isActive":True,
        "isUpdated":False
     },
     {
        "title":"Python Course",
        "description":"Python Course Description",
        "imageUrl":"2.jpg",
        "slug":"python-course",
        "date": date(2023,1,10),
        "isActive":False,
        "isUpdated":False
     },
     {
        "title":"Web Development Course",
        "description":"Web Development Course Description",
        "imageUrl":"3.jpg",
        "slug":"web-development-course",
        "date": date(2023,6,10),
        "isActive":True,
        "isUpdated":True
     }
    ],
    "categories": [
        { "id": 1, "name":"programming", "slug":"programming" }, 
        { "id": 2, "name":"web-development", "slug":"web-development" }, 
        { "id": 3, "name":"mobile-application", "slug":"mobile-application" }, 
    ]
}

def index(request):
    courses = Course.objects.filter(isActive=1)
    categories = Category.objects.all()

    return render(request, "courses/index.html", {'categories': categories, 'courses': courses,})

def details(request, slug):

    course = get_object_or_404(Course, slug=slug)

    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)

def getCoursesByCategoryName(request, slug):
    courses = Course.objects.filter(category__slug=slug, isActive=True)
    categories = Category.objects.all()

    return render(request, 'courses/index.html', {'categories': categories, 'courses': courses, 'selectedCategory': slug})