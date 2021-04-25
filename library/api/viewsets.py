from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from . import models
from . import serializers


class AuthorViewset(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class BookViewset(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        books = models.Book.objects.all()

        name = self.request.GET.get('name')

        if name:
            books = books.filter(name__contains=name)
            
        return books


class EditorialViewset(viewsets.ModelViewSet):
    queryset = models.Editorial.objects.all()
    serializer_class = serializers.EditorialSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = serializers.UserSerializers
    permission_classes = (permissions.IsAuthenticated,)
