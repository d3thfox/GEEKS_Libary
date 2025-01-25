from django.db import models
from django.contrib.auth.models import User

class CustomUsers(User):
    GENDER = (
        ('M','MALE'),
        ('F','FEMALE')
    )
    phone_number = models.CharField(max_length=14)
    experience = models.PositiveIntegerField(default=1)
    gender = models.CharField(max_length=100, choices=GENDER,null=True)
    club = models.CharField(max_length=100)    
    
    
    def save(self, *args, **kwargs):
        if self.experience < 1:
            self.club = 'Ваш опыт слишком мал,вы не подходите'
        elif 1<= self.experience <= 3:
            self.club = '1000$'
        elif 4<= self.experience <= 7:
            self.club = '2000$'
        elif 8<= self.experience <= 10:
            self.club = '5000$'
        else:
            self.club = 'У нас не хватит денег'
        super().save(*args,**kwargs)