from django.db import models
from django.utils import timezone


# Create your models here.
class Editorial(models.Model):
    name = models.CharField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "editorials"


class Author(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "authors"


class Book(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    cover = models.ImageField(upload_to='book/covers/', null=True, blank=True)
    isbn = models.CharField(max_length=20)
    number_pages = models.IntegerField()
    language = models.CharField(max_length=50, default="Español")
    author = models.ForeignKey(Author, related_name='author_books', on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, related_name='editorial_books', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "books"
