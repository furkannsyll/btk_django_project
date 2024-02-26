from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse('Homepage')

def courses(request):
    return HttpResponse('Course List')

urlpatterns = [
    path('', home),
    path('home/', home),
    path('courses/', courses),
    path('admin/', admin.site.urls),
]
