from django.shortcuts import render
from django.views import generic
from . import models

class HastagsAllBookView(generic.ListView):
    template_name = 'hastags/all_books.html'
    context_object_name = 'books'
    model = models.Book
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


# def all_book_view(request):
#     if request.method == 'GET':
#         books = models.Book.objects.all()
#         context = {'books':books}
#         return render(request,template_name='hastags/all_books.html',context=context)

class HastagsFantasticBookView(generic.ListView):
    template_name = 'hastags/fantasy_books.html'
    context_object_name = 'fantasy'
    model = models.Book

    def get_queryset(self):
        return self.model.objects.filter(tags__name = 'Фантастика')




# def fantasy_books(request):
#     if request.method == "GET":
#         fantasy = models.Book.objects.filter(tags__name='Фантастика')
#         context = {'fantasy': fantasy}
#         return render(request,template_name='hastags/fantasy_books.html',context=context)

class HastagsFairyTaleView(generic.ListView):
    template_name = 'hastags/fairy_tale_books.html'
    context_object_name = 'fairy_tale'
    model = models.Book
    
    def get_queryset(self):
        return self.model.objects.filter(tags__name='Сказки')



# def fairy_tale_books(request):
#     if request.method == "GET":
#         fairy_tale = models.Book.objects.filter(tags__name='Сказки')
#         context = {'fairy_tale': fairy_tale}
#         return render(request,template_name='hastags/fairy_tale_books.html',context=context)

class HastagsDramaBookView(generic.ListView):
    template_name = 'hastags/drama_books.html'
    context_object_name = 'drama'
    model = models.Book
    
    def get_queryset(self):
        return self.model.objects.filter(tags__name = 'Драмма')


# def drama_books(request):
#     if request.method == "GET":
#         drama = models.Book.objects.filter(tags__name = 'Драмма')
#         context = {'drama': drama}
#         return render(request,template_name='hastags/drama_books.html',context=context)




