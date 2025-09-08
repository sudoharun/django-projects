from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    is_employed = models.BooleanField(default=False)
    is_contractor = models.BooleanField(default=False)

    def __str__(self):
        return self.username
