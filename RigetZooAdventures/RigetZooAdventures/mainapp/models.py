from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    datetime = models.DateTimeField()
    duration = models.IntegerField(default=0)
    children = models.IntegerField(default=0)
    adults = models.IntegerField(default=0)
    hotel = models.BooleanField(default=False)

    def __str__(self):
        return 'Booking ' + str(self.pk)

class Attraction(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    # Would've added image field here, but forgot and didn't have time :(

    def __str__(self):
        return self.name
