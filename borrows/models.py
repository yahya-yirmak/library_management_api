from django.db import models
from users.models import CustomUser
from books.models import Book
from django.utils.timezone import now

# Create your models here.

class Borrow(models.Model):
    STATUS_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
    ]

    user = models.ForeignKey(CustomUser, related_name='borrowed_books', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='borrow', on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(default=now)
    return_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrowed')

    def __str__(self):
        return f"{self.book.title} borrowed by {self.user.username}"
    
    class Meta:
        ordering = ['-borrow_date']