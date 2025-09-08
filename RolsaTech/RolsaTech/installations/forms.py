from django import forms
from .models import Installation

class CreateInstallationForm(forms.ModelForm):
    class Meta:
        model = Installation
        exclude = ['user']

        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
            }),
            'product': forms.Select(attrs={
                'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
            }),
            'postcode': forms.TextInput(attrs={
                'type': 'text',
                'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
            }),
            'city': forms.TextInput(attrs={
                'type': 'text',
                'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
            }),
            'county': forms.TextInput(attrs={
                'type': 'text',
                'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
            }),
            'first_line': forms.TextInput(attrs={
                'type': 'text',
                'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
            })
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateInstallationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        installation = super().save(commit=False)
        installation.user = self.user
        if commit:
            installation.save()
        return installation
