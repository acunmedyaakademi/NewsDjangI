from django import forms
from .models import Comments

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

