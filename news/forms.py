from django import forms
from .models import Comments, Contact

class CommentsForms(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ('haber',)
        fields = ['name_surname', 'email', 'comment']
        labels = {
            'name_surname': 'İsim Soyisim',
            'email': 'E-posta',
            'comment': 'Yorum',
        }




class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('iletişim',)
        fields = ['name_surname', 'email', 'mesaj']
        labels = {
            'name_surname': 'İsim Soyisim',
            'email': 'E-posta',
            'mesaj': 'Mesaj'
        }


