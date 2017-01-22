from django import forms

class Login_form(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput())


class Register_form(forms.Form):
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=20,widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=20,widget=forms.PasswordInput())