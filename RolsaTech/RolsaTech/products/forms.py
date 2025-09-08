from django import forms
from .models import Product

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget = forms.TextInput(attrs={
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })
        self.fields['description'].widget = forms.Textarea(attrs={
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })
        self.fields['installation_cost'].widget = forms.NumberInput(attrs={
            'step': 0.01,
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })
