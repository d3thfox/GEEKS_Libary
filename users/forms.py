from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
GENDER = (
        ('M','MALE'),
        ('F','FEMALE')
    )
    
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True,label = 'Email')
    phone_number = forms.CharField(required=True, max_length=14,label = 'Номер телефона')
    experience = forms.IntegerField(required=True,label='Введите ваш опыт работы (года)')
    gender = forms.ChoiceField(required=True, choices=GENDER, label='Ваш пол')

    class Meta:
        model = models.CustomUsers
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'experience',
            'gender',
            
        )
    def save(self,commit=True):
        user = super(CustomUserCreationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.experience = self.cleaned_data['experience']
        user.gender = self.cleaned_data['gender']

        if commit:
            user.save()
        return user