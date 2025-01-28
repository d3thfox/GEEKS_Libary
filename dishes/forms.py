from django import forms
from . import models

class RecipeForm(forms.ModelForm):
    class Meta:
        model = models.Recipes
        fields = '__all__'

class IngredientForm(forms.ModelForm):
    class Meta:
        model = models.Ingredients
        fields = '__all__'