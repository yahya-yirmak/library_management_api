from django.shortcuts import render
from django.http import JsonResponse
from .models import Book


def fetch_books(request):
    """ This is a function to return all books instances from Book Model in a JSON format """
    books = Book.objects.all()
    books_data = [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author.first_name + " " + book.author.last_name,
            "category": book.category.name,
            "available_copies": book.available_copies
        }
        for book in books
    ]
    return JsonResponse(books_data, safe=False)



