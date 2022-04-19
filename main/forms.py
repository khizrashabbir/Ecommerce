from django.contrib.auth.models import User
from django import forms
from django.forms import Textarea, CharField

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'user','title', 'review','rating']
        # comment = forms.CharField(widget=forms.Textarea)
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'user': forms.Select(),
                'title': forms.TextInput(attrs={'class':'form-control'}),
                'review': forms.Textarea(attrs={'class':'form-control'}),
                'rating': forms.NumberInput(attrs={'class': 'rating rating-selection'}),

        }

