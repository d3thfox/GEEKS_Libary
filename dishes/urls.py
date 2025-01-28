from django.urls import path
from . import views

urlpatterns = [
    path('create_recipe/',views.RecipeCreateFormView.as_view(), name = 'create_recipe'),
    path('create_ingredient/',views.IngredientCreateFormView.as_view(), name = 'create_ingredient'),
    path('dishes_list/',views.DishesView.as_view(), name ='dishes_list'),
    path('dishes_list/<int:pk>/',views.DishesDetailView.as_view(), name ='dishes_detail'),
    path('dishes_list/<int:id>/delete/',views.DeleteDishesForm.as_view(), name ='delete'),
   
]