from django.urls import path
from . import views

urlpatterns = [
    path('all_books/',views.all_book_view,name = 'all_books'),
    path('drama/',views.drama_books,name= 'drama'),
    path('fantasy/',views.fantasy_books,name= 'fantasy'),
    path('fairy_tail/',views.fairy_tale_books,name= 'fairy_tale'),
]