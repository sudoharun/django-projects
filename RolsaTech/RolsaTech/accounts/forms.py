from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })
        self.fields['first_name'].widget = forms.TextInput(attrs={
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })
        self.fields['last_name'].widget = forms.TextInput(attrs={
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ['old_password', 'new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget = forms.PasswordInput(attrs={
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'type': 'password',
            'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
        })
    )
