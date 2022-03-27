from rest_framework import serializers
from Books.models import Books


class BooksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Books
        fields = ('title','subtitle','author','isbn')
