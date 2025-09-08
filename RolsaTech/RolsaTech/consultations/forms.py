from django import forms
from .models import Consultation

class CreateConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        exclude = ['user']

        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'rounded-md border border-gray-400 inset-shadow-sm bg-gray-100 shadow-md'
            }),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateConsultationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        consultation = super().save(commit=False)
        consultation.user = self.user
        if commit:
            consultation.save()
        return consultation
