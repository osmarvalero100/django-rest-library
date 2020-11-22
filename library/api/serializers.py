from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Author, Book, Editorial


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer): 
    class Meta: 
        model = User 
        fields =  '__all__'
