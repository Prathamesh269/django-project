from django.shortcuts import render
from rest_framework import viewsets
from myapp1.models import Book
from myapp1.serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
# Create your views here.
