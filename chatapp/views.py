# chatapp/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def chatRoom(request, room_name):
    return render(request, 'chat.html', {'room_name': room_name})