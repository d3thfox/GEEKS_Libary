from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def about_me(request):
    if request.method == "GET":
        return HttpResponse("Привет,меня зовут Виталий мне 20 лет.Я учусь backend разработке")

def about_my_pets(request):
    if request.method == "GET":
        return HttpResponse ("<img src='https://www.meme-arsenal.com/memes/9c7e1ef1467cb331e564c0b21f0792f2.jpg'>")

def time_data(request):
    if request.method == "GET":
        current_time = datetime.now()
        return HttpResponse (current_time.strftime("%Y-%m-%d %H:%M:%S"))