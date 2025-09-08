from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Learner)
admin.site.register(Tutor)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Lesson)