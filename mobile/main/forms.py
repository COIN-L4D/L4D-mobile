from django import forms

from .models import Context

class ContextForm(forms.ModelForm):
    class Meta:
        model = Context
        fields = ['quest']
