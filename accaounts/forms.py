from django import forms
from django.forms.widgets import TextInput, PasswordInput, EmailInput
from django.contrib.auth.forms import UserCreationForm




# class EmailSignupForm(forms.Modelform):
#     class Meta:
#         model=Signup
#         fields=('email',)

class loginForm(forms.Form):
    username=forms.CharField(
        max_length=30,
        widget=TextInput(attrs={
            'name':'username',
            'class':'form-control',
            'placeholder':'username',
            'required':'required'
        })
    )
    password=forms.CharField(
        widget=PasswordInput(attrs={
            'name':'password',
            'class':'form-control',
            'placeholder':'password',
            'required':'required'
        })
    )
class registerForm(forms.Form):
    first_name=forms.CharField(
        max_length=30,
        widget=TextInput(attrs={
            'name':'first_name',
            'class':'form-input',
            'placeholder':'Name',
            'required':'required'
        })
    )
    last_name=forms.CharField(
        max_length=30,
        widget=TextInput(attrs={
            'name':'last_name',
            'class':'form-input',
            'placeholder':'Last Name',
            'required':'required'
        })
    )
    username=forms.CharField(
        max_length=30,
        widget=TextInput(attrs={
            'name':'username',
            'class':'form-input',
            'placeholder':'username',
            'required':'required'
        })
    )
    email=forms.EmailField(
        widget=EmailInput(attrs={
            'name':'email',
            'class':'form-input',
            'placeholder':'E-mail',
            'required':'required'
        })
    )
    password1=forms.CharField(
        widget=PasswordInput(attrs={
            'name':'password1',
            'class':'form-input',
            'placeholder':'password',
            'required':'required',
            'id':'password'
        })
    )
    password2=forms.CharField(
        widget=PasswordInput(attrs={
            'name':'password2',
            'class':'form-input',
            'placeholder':'re-password',
            'required':'required'
        })
    )