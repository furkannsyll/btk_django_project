from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from books.models import Book
from books.serializer import BookSerializer

@api_view(['GET'])
def book_list(request):
   books = Book.objects.all()
   serializer = BookSerializer(books, many=True)
   return Response(serializer.data)

def create(request):
    pass

