from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Booking, Attraction, User

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['datetime', 'duration', 'adults', 'children', 'hotel']
        exclude = ['user']

        labels = {
            'datetime': _('Please enter a date and time for your booking:'),
            'duration': _('Please enter the number of days you wish your visit will last:'),
            'adults': _('Please enter the number of adults that will attend:'),
            'children': _('Please enter the number of children that will attend:'),
            'hotel': _('Please select this checkbox if you want to book a stay at the hotel (will automatically be the same as your booking duration):')
        }

        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'rounded bg-alt border-2 border-gray-500'}),
            'duration': forms.NumberInput(attrs={'class': 'rounded bg-alt border-2 border-gray-500'}),
            'adults': forms.NumberInput(attrs={'class': 'rounded bg-alt border-2 border-gray-500'}),
            'children': forms.NumberInput(attrs={'class': 'rounded bg-alt border-2 border-gray-500'}),
            'hotel': forms.CheckboxInput(attrs={'class': 'rounded bg-alt border-2 border-gray-500'})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        booking = super().save(commit=False)

        if self.user is not None:
            if not self.user.is_superuser:
                booking.user = self.user

        if commit:
            booking.save()

        return booking

class AttractionForm(forms.ModelForm):
    class Meta:
        model = Attraction
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'rounded bg-alt border-2 border-gray-500'}),
            'description': forms.Textarea(attrs={'class': 'rounded bg-alt border-2 border-gray-500'})
        }

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'rounded bg-alt border-2 border-gray-500'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'rounded bg-alt border-2 border-gray-500'}))

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password2 = cleaned_data['password2']

        if password and password2 and password != password2:
            raise forms.ValidatonError('Passwords do not match!')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'rounded bg-alt border-2 border-gray-500'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'rounded bg-alt border-2 border-gray-500'}))
