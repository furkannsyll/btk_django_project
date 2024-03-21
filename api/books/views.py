from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from books.models import Book
from books.serializer import BookSerializer
from rest_framework import status

@api_view(['GET'])
def book_list(request):
   books = Book.objects.all()
   serializer = BookSerializer(books, many=True)
   return Response(serializer.data)

@api_view(['GET'])
def book (request, id):
    try:
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except:
        return Response({"error":"Matching record not found"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['PUT'])   
def book_update(request, id):
    book = Book.objects.get(pk=id)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
@api_view(['DELETE'])   
def book_delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)

