from django import forms

from . import models

class CreatePersoneFrom(forms.ModelForm):
    phones = forms.CharField(widget=forms.Textarea(), help_text="separated by new line'//n")
    class Meta:
        model = models.Persone
        fields = (
            'name',
            'phones'
        )