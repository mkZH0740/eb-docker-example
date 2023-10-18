from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def create_user(request):
    if User.objects.get(username="bob") is None:
        User.objects.create_user(username="bob", email="123@qew.com", password="1!2!3!4!5!6!7!8!")
    return HttpResponse("")