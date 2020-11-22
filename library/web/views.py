from django.shortcuts import render
from api.models import Book

# Create your views here.
def home(request):
    book_exist = Book.objects.all()[:1]
    return render(request, 'web/book/index.html', {"book_exist": book_exist})


def book_detail(request, id):
    return render(request, 'web/book/detail.html', {"book_id": id})
