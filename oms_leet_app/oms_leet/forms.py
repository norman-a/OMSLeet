from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=120, required=True,
                             help_text="Email must end with gatech.edu")
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
