from django import forms
from django.forms import ModelForm

from .models import User


class UserFormRegister(ModelForm):

    class Meta:

        model = User
        fields = '__all__'


class UserFormLogin(forms.Form):

    username = forms.CharField(label='Username', max_length=255)
    password = forms.CharField(label='Password', max_length=255)