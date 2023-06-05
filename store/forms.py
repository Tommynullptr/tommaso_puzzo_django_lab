from django import forms


class UserFormRegister(forms.Form):

    username = forms.CharField(label='Username', max_length=255)
    firstname = forms.CharField(label='First Name', max_length=255)
    lastname = forms.CharField(label='Last Name', max_length=255)
    password = forms.CharField(label='Password', max_length=255)
    address = forms.CharField(label='Address', max_length=255)
    city = forms.CharField(label='City', max_length=255)
    state = forms.CharField(label='State', max_length=255)


class UserFormLogin(forms.Form):

    username = forms.CharField(label='Username', max_length=255)
    password = forms.CharField(label='Password', max_length=255)