from django.shortcuts import render
from rest_framework.decorators import api_view
import json
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
# Create your views here.
@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['GET'])
def list_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_book(request, id):
    book = Book.objects.get(id=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['PUT'])
def update_book(request, id):
    book = Book.objects.get(id=id)
    serializer = BookSerializer(book, data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return Response({"message": "Book deleted successfully"})