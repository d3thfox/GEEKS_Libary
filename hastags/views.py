from django.shortcuts import render

from . import models

def fantasy_books(request):
    if request.method == "GET":
        fantasy = models.Book.objects.filter(tags__name='Фантастика')
        context = {'fantasy': fantasy}
        return render(request,template_name='hastags/fantasy_books.html',context=context)

def fairy_tale_books(request):
    if request.method == "GET":
        fairy_tale = models.Book.objects.filter(tags__name='Сказки')
        context = {'fairy_tale': fairy_tale}
        return render(request,template_name='hastags/fairy_tale_books.html',context=context)

def drama_books(request):
    if request.method == "GET":
        drama = models.Books.objects.filter(tags__name = 'Драма')
        context = {'drama': drama}
        return render(request,template_name='hastags/drama_books.html',context=context)




