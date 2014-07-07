'''
Created on 06-Jul-2014

@author: sanatan
'''
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    firstName = forms.CharField()
    lastName = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    repassword = forms.CharField(widget=forms.PasswordInput())
    contact = forms.IntegerField()
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())