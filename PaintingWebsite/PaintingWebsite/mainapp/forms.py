from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "email", "time", "teacher"]
        field_order = ["name", "email", "teacher", "time"]
        widgets = {
            "time": forms.DateTimeInput(attrs={"placeholder": "Enter a Date and Time in this format: YYYY-MM-DD HH:MM:SS"}),
        }