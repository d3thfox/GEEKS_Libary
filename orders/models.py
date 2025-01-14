from django.db import models
from library.models import Books

class OrderModel(models.Model):
    PAY_CHOICE = (
        ('Mbank','Mbank'),
        ('Optima','Optima'),
        ('Finca Bank ','Finca Bank'),
        ('При доставке','При доставке'),
    )
    choice_book = models.ForeignKey(Books,on_delete=models.CASCADE,verbose_name='Выберите книгу',null=True)
    user_adress = models.TextField(verbose_name='Введите ваш адресс')
    pay = models.CharField(max_length=20,choices=PAY_CHOICE,verbose_name='Выберите способ оплаты',null=True)
    card_number = models.PositiveIntegerField(verbose_name='Введите номер карты')
    phone_number = models.PositiveIntegerField(verbose_name='Введите номер телефона')

    def __str__(self):
        return f'{self.choice_book.book_title}-{self.choice_book.price}'



