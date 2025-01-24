from django import forms
from . import models, parser_mybook

class ParserForm(forms.Form):
    LIBARY_CHOICES = (
        ('mybook', 'mybook'),
        ('readlove', 'readlove'),
    )
    libary_type = forms.ChoiceField(choices=LIBARY_CHOICES)

    class Meta:
        fields = [
            'libary_type', 
        ]
    
    def parser_data(self):
        if self.cleaned_data['libary_type'] == 'mybook':
            mybook_file = parser_mybook.parsing()
            
            for i in mybook_file:
                models.MyBookParser.objects.create(**i)
