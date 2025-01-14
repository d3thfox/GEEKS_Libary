from django.shortcuts import render

from . import models

def all_book_view(request):
    if request.method == 'GET':
        books = models.Book.objects.all()
        context = {'books':books}
        return render(request,template_name='hastags/all_books.html',context=context)


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
        drama = models.Book.objects.filter(tags__name = 'Драмма')
        context = {'drama': drama}
        return render(request,template_name='hastags/drama_books.html',context=context)




