from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

from userAccuntApp.models import Guest



class GuestForm(forms.ModelForm):
    class Meta:
        model= Guest
        fields = "__all__"



class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = {'first_name','last_name','username','email','password1','password2'}

        

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class UpdateUserForm(forms.ModelForm):

    passwird = None

    class Meta:
        model= User
        fields = ['username', 'email']
        exclude =['password1','password2']