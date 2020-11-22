from django.urls import path
from .views import home, book_detail

urlpatterns = [
    path('', home, name="home"),
    path('book/detail/<int:id>/', book_detail, name="book_detail"),
]