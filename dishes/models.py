from django.db import models
from django.db.models import ForeignKey
CHOICE_UNIT = (
    ('грамм','грамм'),
    ('киллограмм','киллограмм'),
    ('миллилитров','миллилитров'),
    ('литров','литров'),
    ('штук','штук'),
)

class Recipes(models.Model):
    title = models.CharField(max_length= 100,verbose_name='Введите название')
    description = models.TextField(verbose_name='Введите описание рецепта')

    def __str__(self):
        return self.title

class Ingredients(models.Model):
    name = models.CharField(max_length= 100,verbose_name='Введите название ингридиента')
    quantity = models.IntegerField(verbose_name='Количество')
    unit = models.CharField(max_length= 100,verbose_name = 'Выберите единицу измерения',
                            choices=CHOICE_UNIT,)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name='Выберите рецепт')

    def __str__(self):
        return self.name

