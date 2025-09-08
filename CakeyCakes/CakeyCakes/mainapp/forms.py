from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Cake, Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'image_link', 'ingredients', 'recipe', 'gluten_free')
        field_order = ('name', 'description', 'image_link', 'ingredients', 'recipe', 'gluten_free')

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form_control',
                'rows': 3,
                'placeholder': 'Enter the Recipe description',
            }
        )
    )

    ingredients = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form_control',
                'rows': 5,
                'placeholder': 'Enter the Recipe ingredients, comma separated',
            }
        )
    )

    recipe = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form_control',
                'rows': 5,
                'placeholder': 'Enter the actual Recipe',
            }
        )
    )

class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ('name', 'description', 'recipe')
        field_order = ('name', 'description', 'recipe')

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form_control',
                'rows': 3,
                'placeholder': 'Enter the Cake description',
            }
        )
    )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class CustomUserChangeForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
