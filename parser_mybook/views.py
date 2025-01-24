
from django.http import HttpResponse
from django.shortcuts import render
from . import models, forms
from django.views import generic

class MyBookListView(generic.ListView):
    template_name = 'parser/mybook_list.html'
    context_object_name = 'my_book'
    model = models.MyBookParser

    def get_queryset(self):
        return self.model.objects.all()
    
class MyBookFormView(generic.FormView):
    template_name = 'parser/mybook_form.html'
    form_class = forms.ParserForm

    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Парсер успешно завершен')
        else:
            return super(MyBookFormView, self).post(request,*args,**kwargs)


