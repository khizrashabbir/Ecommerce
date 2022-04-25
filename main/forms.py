from django.contrib.auth.models import User
from django import forms
from django.forms import Textarea, CharField

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'user','title', 'product','review','rating']

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['user'].widget.attrs.update({'class': 'form-control '})
        # comment = forms.CharField(widget=forms.Textarea)
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                # 'user': forms.Select(attrs={'readonly'}),
                'user': forms.Select(attrs={'class': 'hidden'}),
                'product': forms.Select(attrs={'class': 'hidden'}),
                'title': forms.TextInput(attrs={'class':'form-control'}),
                'review': forms.Textarea(attrs={'class':'form-control'}),
                'rating': forms.NumberInput(attrs={'class': 'review-star','type': 'hidden','id':'total'}),

        }

