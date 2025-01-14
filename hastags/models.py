from django.db import models

from library.models import Books


class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

class Book(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    class Meta:
         verbose_name = "книга"
         verbose_name_plural = "книги"





