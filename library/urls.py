from django.urls import path
from . import views

urlpatterns = [
    path('about_me/',views.about_me,name='about_me'),
    path('about_my_pets/',views.about_my_pets,name='about_my_pets'),
    path('time_data/',views.time_data,name='time_data'),
]