from django.shortcuts import render,redirect,get_object_or_404
from . import models,forms

def choice_book_view(request):
    if request.method == 'POST':
        form = forms.OrderForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = forms.OrderForm()
    return render(request,template_name='orders/create_order.html',context={'form':form})      

def order_list_view(request):
    if request.method == 'GET':
        order_list = models.OrderModel.objects.all().order_by('-id')
        context = {'order_list': order_list}
        return render(request,template_name='orders/order_list.html',context=context)    
    
def order_detail_view(request,id):
    if request.method == 'GET':
        order_id = get_object_or_404(models.OrderModel,id = id)
        context = {'order_id': order_id}
        return render(request,template_name="orders/order_detail.html",context=context)
    
def order_delete_view(request,id):
    order_id = get_object_or_404(models.OrderModel,id = id)
    order_id.delete()
    return redirect('order_list')
    


