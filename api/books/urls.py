from django.urls import path
from . import views

urlpatterns = [
    path('', views.create),
    path('list/', views.book_list),
]
