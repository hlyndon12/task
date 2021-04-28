from django.forms import ModelForm
from django import forms
from .models import userModel, pushNotifications


class UserForm(ModelForm):
    class Meta:
        model = userModel
        fields = ['Icon', 'username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PushForm(ModelForm):
    class Meta:
        model = pushNotifications
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
        }