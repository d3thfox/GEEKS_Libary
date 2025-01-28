from django.shortcuts import render,redirect,get_object_or_404
from . import models,forms
from django.views import generic

class RecipeCreateFormView(generic.CreateView):
    template_name = 'dishes/create_recipe.html'
    form_class = forms.RecipeForm
    success_url = '/dishes_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form = form)

class IngredientCreateFormView(generic.CreateView):
    template_name = 'dishes/create_ingredient.html'
    form_class = forms.IngredientForm
    success_url = '/dishes_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form = form)



class DishesView(generic.ListView):
    template_name = 'dishes/dishes_list.html'
    context_object_name = 'dishes'
    model = models.Recipes

    def get_queryset(self):
        return self.model.objects.all()
    
class DishesDetailView(generic.DetailView):
    template_name = 'dishes/dishes_detail.html'
    context_object_name = 'recipe'
    model = models.Recipes

    def get_object(self,**kwargs):
        return get_object_or_404(models.Recipes,pk = self.kwargs.get('pk'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = context['recipe']
        ingredients = models.Ingredients.objects.filter(recipe=recipe)
        context['ingredients'] = ingredients
        return context    
    
class DeleteDishesForm(generic.DeleteView):
     template_name = 'dishes/confirm_delete.html'
     success_url = '/dishes_list/'

     def get_object(self):
          recipes_id = self.kwargs.get('id')
          return get_object_or_404(models.Recipes,id = recipes_id) 

