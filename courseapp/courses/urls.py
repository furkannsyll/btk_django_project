from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses),
    path('list/', views.courses),
    path('details/', views.details),
    path('<category>', views.getCoursesByCategory),
]
