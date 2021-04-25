from django.db.models.query import QuerySet
from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Author, Book, Editorial        
class EditorialSerializer(serializers.ModelSerializer):
    #editorial_books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Editorial
        fields = (
            'id',
            'name',
           # 'editorial_books',
        )

class AuthorSerializer(serializers.ModelSerializer):
    #author_books = BookSerializer(many=True, read_only=True) 
    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'email',
            #'author_books',
        )

class BookSerializer(serializers.ModelSerializer):
    # book_author = serializers.CharField(source='author.name', read_only=True)
    # book_editorial = serializers.CharField(source='editorial.name', read_only=True)
    editorial = EditorialSerializer(read_only=True)
    editorial_id = serializers.PrimaryKeyRelatedField(queryset=Editorial.objects.all(), source="editorial")
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source="author")

    def validate_name(self, value):
        exist = Book.objects.filter(name__iexact=value).exists()

        if exist:
            raise serializers.ValidationError('Este libro ya existe')
            
        return value
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer): 
    class Meta: 
        model = User 
        fields =  '__all__'

