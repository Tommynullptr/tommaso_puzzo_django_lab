from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from .models import CustomUser


class UserFormRegister(ModelForm):

    class Meta:

        model = CustomUser
        fields = '__all__'


class UserFormLogin(forms.Form, AuthenticationForm):

    username = forms.CharField(label='Username', max_length=255)
    password = forms.CharField(label='Password', max_length=255)