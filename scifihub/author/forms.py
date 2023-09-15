from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class AuthorCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', ]

