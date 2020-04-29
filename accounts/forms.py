from django.contrib.auth import forms as auth_forms
from django import forms
from . import models


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = models.User
        fields = ('username', 'email', 'password1', 'password2')
