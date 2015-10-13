from django import forms

from .models import Context

class ContextForm(forms.ModelForm):
    class Meta:
        model = Context
        fields = ['quest']

class PasswordForm(forms.Form):
    password = forms.CharField(max_length=512,
        widget=forms.TextInput(attrs={'placeholder': 'Password'}))
