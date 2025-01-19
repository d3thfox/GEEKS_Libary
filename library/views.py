from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from datetime import datetime
from . import models,forms
from django.views import generic
from django.views.generic import ListView

class SearchBooksView(ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return models.Books.objects.filter(book_title__icontains=self.request.GET.get('q'))
                                           
    def get_context_data(self, *, object_list = None ,**kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context



# #Не полная информация о книге
class LibaryBookListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    model = models.Books


    def get_queryset(self):
        return self.model.objects.all().order_by('-id')




# def book_list(request):
#     if request.method == "GET":
#         book_list = models.Books.objects.all().order_by('-id')
#         context = {'book_list': book_list}
#         return render(request,template_name='book.html', context=context)
class LibaryBookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self,**kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=book_id)
    


# def book_detail(request,id):
#     if request.method == "GET":
#         book_id = get_object_or_404(models.Books, id=id)
#         context = {'book_id': book_id}
#         return render(request,template_name='book_detail.html', context=context)
class CreateCommentView(generic.CreateView):
    template_name = 'comments/create_comments.html'
    form_class = forms.CommentForm
    success_url = '/create_comment/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form = form)




# def create_comments_view(request):
#     if request.method == 'POST':
#         form = forms.CommentForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = forms.CommentForm()
#     return render(request,template_name='comments/create_comments.html',context={'form':form})   









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