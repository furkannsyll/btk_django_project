from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.book),
    path('create/', views.book_create),
    path('update/<int:id>', views.book_update),
    path('delete/<int:id>', views.book_delete),
    path('list/', views.book_list),
]
