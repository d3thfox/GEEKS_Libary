from django.urls import path
from . import views

urlpatterns = [
    path('create_order/',views.choice_book_view,name = 'create_order'),
    path('order_list/',views.order_list_view,name = 'order_list'),
    path('order_list/<int:id>/',views.order_detail_view,name = 'order_detail'),
    path('order_list/<int:id>/delete/',views.order_delete_view,name = 'order_delete')


]
