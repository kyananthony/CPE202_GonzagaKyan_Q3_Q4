from django import forms
from django.contrib.auth.models import UserCreationForm
from django.contrib.auth.forms import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', '<PASSWORD>', '<PASSWORD>']
