from django import forms
from .models import Comments

class CommentsForms(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ('News',)

