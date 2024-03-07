from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.details, name="course_details"),
    path('category/<slug:slug>', views.getCoursesByCategoryName, name='courses_by_category'),
]