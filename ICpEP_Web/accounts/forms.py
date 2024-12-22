"""
forms.py is responsible for handling the user input. It receives the input of the user, validates them,
and secures them before putting these data to the database
"""


from django import forms
from django.contrib.auth.forms import UserCreationForm # Using default form maker
from .models import CustomUser # Using the custom user model
from django.contrib.auth import authenticate

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use your custom user model
        fields = ['given_name', 'last_name', 'email', 'password1', 'password2', 'role', 'acad_year', 'acad_block', 'membership_id', 'student_id']


class LoginForm(forms.Form):
    """
    This is the form presented when the user wants to log in
    """
    username = forms.CharField(max_length=150, label='Email')  # Use email as the username
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('Invalid username or password.')

        return cleaned_data
