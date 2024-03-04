from datetime import date
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

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
        "imageUrl":"https://img-c.udemycdn.com/course/750x422/1662526_fc1c_3.jpg",
        "slug":"javascript-course",
        "date": date(2022,10,10),
        "isActive":True,
        "isUpdated":False
     },
     {
        "title":"Python Course",
        "description":"Python Course Description",
        "imageUrl":"https://img-c.udemycdn.com/course/750x422/2463492_8344_3.jpg",
        "slug":"python-course",
        "date": date(2023,1,10),
        "isActive":False,
        "isUpdated":False
     },
     {
        "title":"Web Development Course",
        "description":"Web Development Course Description",
        "imageUrl":"https://img-c.udemycdn.com/course/750x422/1258436_2dc3_4.jpg",
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
    # 2nd Alternative
    # courses = []
    # categories = db["categories"]

    # for course in db["courses"]:
    #     if course["isActive"] == True:
    #         courses.append(course)

    # list comprehension
    courses = [course for course in db["courses"] if course["isActive"]==True]
    categories = db["categories"]

    return render(request, "courses/index.html", {'categories': categories, 'courses': courses,})

def details(request, course_name):
    return HttpResponse(f"{course_name} detail page")

def getCoursesByCategoryName(request, category_name):
    try:
        category_text = data[category_name]
        return render(request, "courses/courses.html", {'category': category_name, 'category_text': category_text} )
    except:
        return HttpResponseNotFound('<h1>False Category Selection</h1>')

def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound('False Category Selection')
    category_name = category_list[category_id - 1]

    redirect_url = reverse('courses_by_category', args=[category_name])
    
    return redirect(redirect_url)