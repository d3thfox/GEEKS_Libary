from django.shortcuts import render,redirect,get_object_or_404
from . import models,forms
from django.views import generic



class OrderBookView(generic.CreateView):
    template_name = 'orders/create_order.html'
    form_class = forms.OrderForm
    success_url = '/create_order/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form = form)

# def choice_book_view(request):
#     if request.method == 'POST':
#         form = forms.OrderForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('order_list')
#     else:
#         form = forms.OrderForm()
#     return render(request,template_name='orders/create_order.html',context={'form':form})      


class OrderListView(generic.ListView):
    template_name = 'orders/order_list.html'
    context_object_name = 'order_list'
    model = models.OrderModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
# def order_list_view(request):
#     if request.method == 'GET':
#         order_list = models.OrderModel.objects.all().order_by('-id')
#         context = {'order_list': order_list}
#         return render(request,template_name='orders/order_list.html',context=context)    


class OrderDetailView(generic.DetailView):
    template_name = 'orders/order_detail.html'
    context_object_name = 'order_id'
    model = models.OrderModel

    def get_object(self,**kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(models.OrderModel, id=order_id)
# def order_detail_view(request,id):
#     if request.method == 'GET':
#         order_id = get_object_or_404(models.OrderModel,id = id)
#         context = {'order_id': order_id}
#         return render(request,template_name="orders/order_detail.html",context=context)
    
class DeleteOrderForm(generic.DeleteView):
     template_name = 'orders/confirm_delete.html'
     success_url = '/order_list/'

     def get_object(self):
          order_id = self.kwargs.get('id')
          return get_object_or_404(models.OrderModel,id = order_id)
    
# def order_delete_view(request,id):
#     order_id = get_object_or_404(models.OrderModel,id = id)
#     order_id.delete()
#     return redirect('order_list')
    


