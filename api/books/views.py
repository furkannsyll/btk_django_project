from django.shortcuts import render
from django.http import JsonResponse
from books.models import Book

def book_list(request):
   books = Book.objects.all()
   books_list = list(books.values())
   return JsonResponse({
    #    "books": ["book 1, book 2"]
    #    "books": [
    #        {"id":1,"title":"book 1"},
    #        {"id":2,"title":"book 2"},
    #    ]
        "books": books_list
   })

def create(request):
    pass

