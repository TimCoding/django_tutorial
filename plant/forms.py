from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    #Widget helps protect the password
    password = forms.CharField(widget=forms.PasswordInput)

    #Contains info about your class
    class Meta:
        model = User
        fields = ['username', 'email', 'password']