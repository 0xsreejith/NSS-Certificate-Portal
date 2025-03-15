from django import forms
from .models import Certificate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CertificateUploadForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['student', 'file']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
