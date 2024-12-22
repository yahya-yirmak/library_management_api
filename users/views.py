from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import CustomUser

def user_list(request):
    users = CustomUser.objects.all()  # Get all users
    user_data = [{"id": user.id, "phone": user.phone, "role": user.role} for user in users]  # Format user data
    return JsonResponse({"users": user_data})
