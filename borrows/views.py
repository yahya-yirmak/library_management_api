from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from .models import Borrow, Book
import json

@csrf_exempt
def borrow_book(request):
    if request.method == "POST":
        data = json.loads(request.body)
        book_id = data.get("book")
        member_id = data.get("member")
        return_date = data.get("return_date")
        
        try:
            book = Book.objects.get(id=book_id)
            if book.available_copies <= 0:
                return JsonResponse({"error": "No copies available"}, status=400)
            
            book.available_copies -= 1
            book.save()
            
            borrow = Borrow.objects.create(
                book=book,
                member_id=member_id,
                return_date=parse_date(return_date)
            )
            return JsonResponse({
                "id": borrow.id,
                "book": borrow.book.title,
                "member": borrow.member.username,
                "borrow_date": borrow.borrow_date,
                "return_date": borrow.return_date
            }, status=201)
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)
