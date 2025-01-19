from django.urls import path
from . import views

urlpatterns = [
    path('create_order/',views.OrderBookView.as_view(),name = 'create_order'),
    path('order_list/',views.OrderListView.as_view(),name = 'order_list'),
    path('order_list/<int:id>/',views.OrderDetailView.as_view(),name = 'order_detail'),
    path('order_list/<int:id>/delete/',views.DeleteOrderForm.as_view(),name = 'order_delete')


]
