from django.db import models
from django.db.models import ForeignKey


class Books(models.Model):
    GENRE_CHOICES = (
        ('Комедия','Комедия'),
        ('Ужасы','Ужасы'),
        ('Дарк фентези','Дарк фентези'),
        ('Антиутопия','Антиутопия'),

    )
    picture = models.ImageField(upload_to='movies/',verbose_name='Загрузите фото',null=True)
    book_title = models.CharField(max_length=100,verbose_name='Введите название книги')
    description = models.TextField(verbose_name="Введите описание книги",blank=True,null=True)
    price = models.PositiveIntegerField(verbose_name='Укажите цену',default=200)
    created_at = models.DateTimeField(auto_now_add=True)
    genre_choice = models.CharField(max_length=100,verbose_name='Укажите жанр',choices=GENRE_CHOICES)
    email_author = models.EmailField(verbose_name='Введите адрес почты',blank=True,null=True)
    author = models.CharField(max_length=100,verbose_name='Введите имя автора')
    overview_link = models.URLField(verbose_name='Укажите ссылку с YouTube',blank=True,null=True)

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return f'{self.book_title} - {self.price} сом'

class Reviews(models.Model):
    CHOICES_STAR = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')
    )
    review_choice = models.ForeignKey(Books,on_delete=models.CASCADE,
                                      related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(verbose_name='Напишите как вам книга')
    stars = models.CharField(max_length=100,choices=CHOICES_STAR,default='⭐⭐⭐⭐⭐')

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural ='комментарии'

    def __str__(self):
        return f'{self.review_choice.book_title} - {self.comment}'
    
















