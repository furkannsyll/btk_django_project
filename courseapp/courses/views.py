from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programming":"Courses in the Programming Category",
    "web-development":"Courses in the Web Development Category",
    "mobile":"Courses in the Mobile Category"
}

def courses(request):
    return HttpResponse('Course List')

def details(request, course_name):
    return HttpResponse(f"{course_name} detail page")

def getCoursesByCategoryName(request, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound('False Category Selection')

def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound('False Category Selection')
    category_name = category_list[category_id - 1]

    redirect_url = reverse('courses_by_category', args=[category_name])
    
    return redirect(redirect_url)