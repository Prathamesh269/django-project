from rest_framework import serializers
from myapp1.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = ['id','title','author','publish_date']