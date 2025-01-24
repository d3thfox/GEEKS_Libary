from django.db import models

class MyBookParser(models.Model):
    title = models.CharField(max_length=200)
    href = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title
