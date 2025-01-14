from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book_detail/<int:id>/', views.book_detail, name='book_detail'),
    path('about_me/',views.about_me,name='about_me'),
    path('about_my_pets/',views.about_my_pets,name='about_my_pets'),
    path('time_data/',views.time_data,name='time_data'),
    path('create_comment/',views.create_comments_view,name = 'create_comment'),

]