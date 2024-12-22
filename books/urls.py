from django.urls import path
from .views import fetch_books

urlpatterns = [
    path('api/books/', fetch_books, name='fetch_books'),
]
