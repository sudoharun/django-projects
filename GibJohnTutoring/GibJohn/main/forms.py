from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Subject, Course, Lesson

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "first_name", "last_name", "email")

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=225, required=True, widget=forms.TextInput(attrs={
        "placeholder": "Enter your username here...",
        "class": "border-2 border-alt bg-white"
    }))
    password = forms.CharField(label="Password", max_length=225, required=True, widget=forms.PasswordInput(attrs={
        "placeholder": "Enter your password here...",
        "class": "border-2 border-alt bg-white"
    }))

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ("title",)

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "subject", "description")
        field_order = ("title", "subject", "description")

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ("title", "course", "content")
        field_order = ("title", "course", "content")
        labels = {
            "content": "Lesson Content",
        }
        widgets = {
            "content": forms.Textarea(attrs={
                "row": 32,
                "cols": 64,
                "placeholder": "Enter the lesson content here...",
                "class": "border-2 border-alt bg-white"
            })
        }