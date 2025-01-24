from django.urls import path
from . import views

urlpatterns = [
    path('mybook_list/',views.MyBookListView.as_view(),name = 'mybook_list'),
    path('mybook_form/',views.MyBookFormView.as_view(),name = 'mybook_form'),
]