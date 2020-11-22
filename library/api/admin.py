from django.contrib import admin
from .models import Editorial, Author, Book


class BookAdmin(admin.ModelAdmin):
    search_fields = ["name", "description"]
    list_filter = ["editorial"]
    list_per_page = 10


# Register your models here.
admin.site.register(Editorial)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
