from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.book),
    path('create/', views.book_create),
    path('list/', views.book_list),

]
