from django import forms
from .models import UserSignIn,UserSignUp

class Sign_In(forms.ModelForm):
    class Meta:
        model = UserSignIn
        fields = ['email', 'password']

class Sing_Up(forms.ModelForm):
    class Meta:
        model = UserSignUp
        fields = ['nome','email','password']

        