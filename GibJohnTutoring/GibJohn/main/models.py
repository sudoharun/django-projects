from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tutor')

    class Meta:
        permissions = (
            ('can_view_own_models', 'View own models'),
            ('can_view_tutor_dashboard', 'Go to dashboard'),
            # Course related permissions
            ('can_create_own_course', 'Create a new course'),
            ('can_edit_own_course', 'Edit one of your existing courses'),
            ('can_delete_own_course', 'Delete one of your existing courses'),
            # Lesson related permissions
            ('can_create_own_lesson', 'Create a new lessons'),
            ('can_edit_own_lesson', 'Edit one of your existing lessons'),
            ('can_delete_own_lesson', 'Delete one of your existing lessons'),
            # More account-related permissions
            # ('add_course_to_account', 'Add course to your account'),
            # ('remove_course_from_account', 'Remove course from account'),
        )
    
    def __str__(self):
        return self.user.username

    def clean(self):
        if not self.user:
            raise ValidationError("A user must be assigned to this tutor")

class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='learner')

    class Meta:
        permissions = (
            # Account-related permissions
            ('add_course_to_account', 'Add course to your account'),
            ('remove_course_from_account', 'Remove course from account'),
            ('can_view_learner_dashboard', 'Go to dashboard'),
        )
    
    def __str__(self):
        return self.user.username

    def clean(self):
        if not self.user:
            raise ValidationError("A user must be assigned to this learner")

class Subject(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=225, null=True)
    author = models.ForeignKey(Tutor, null=True, on_delete=models.SET_NULL, related_name='courses')
    date_posted = models.DateField(default=datetime.today())
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    learners = models.ManyToManyField(Learner, related_name="courses", blank=True)

    def __str__(self):
        return self.title

    def clean(self):
        if not self.subject:
            raise ValidationError("A subject must be assigned to this course")

class Lesson(models.Model):
    title = models.CharField(max_length=64)
    date_posted = models.DateField(default=datetime.today())
    author = models.ForeignKey(Tutor, null=True, on_delete=models.SET_NULL, related_name='lessons')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    content = models.TextField()

    def __str__(self):
        return self.title

    def clean(self):
        if not self.course:
            raise ValidationError("A course must be assigned to this lesson")