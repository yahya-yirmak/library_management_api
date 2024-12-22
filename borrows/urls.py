from django.urls import path
from .views import borrow_book

urlpatterns = [
    path('api/borrows/', borrow_book, name='borrow_book'),
]
