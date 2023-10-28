from django.shortcuts import render
from .models import User,Message
from django.http import HttpResponse


def chat_room(request):
    context = Message.objects.all()

    return render(request, 'chatapp/chat.html', {'Messages':context})


def chat_home(request):
    return HttpResponse('Welcome to Chat Room App')
