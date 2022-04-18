from django.contrib.auth.models import User
from django import forms
from .models import Review


class ReviewForm(forms.Form):
    model = Review
