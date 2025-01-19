from django.urls import path
from . import views

urlpatterns = [
    path('all_books/',views.HastagsAllBookView.as_view(),name = 'all_books'),
    path('drama/',views.HastagsDramaBookView.as_view(),name= 'drama'),
    path('fantasy/',views.HastagsFantasticBookView.as_view(),name= 'fantasy'),
    path('fairy_tail/',views.HastagsFairyTaleView.as_view(),name= 'fairy_tale'),
]