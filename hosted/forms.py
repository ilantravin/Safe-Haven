from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    CATEGORY_CHOICES = [
        ('hosted', 'מתארח'),
        ('host', 'מארח'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='קטגוריה')  # Hebrew for 'category'
    email = forms.EmailField(required=True, label='אימייל')  # Hebrew for 'email'

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'category')  # Add 'email' here