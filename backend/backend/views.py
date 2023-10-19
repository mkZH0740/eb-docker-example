from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def create_user(request):
    if not User.objects.filter(username="bob").exists():
        User.objects.create_user(username="bob", email="123@qew.com", password="1!2!3!4!5!6!7!8!")
    return HttpResponse("")