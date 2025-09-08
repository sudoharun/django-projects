from django.db import models
from datetime import datetime

TEACHERS = (
    ("JW", "James Williams"),
    ("HG", "Hana Goodwill"),
    ("SJ", "Sarah Jones"),
    ("CS", "Chad Smith"),
    ("LS", "Luis Suarez"),
    ("LJ", "LeBron James"),
)

# Create your models here.
class Painting(models.Model):
    name = models.CharField(max_length=225)
    artist = models.CharField(max_length=225)
    date_painted = models.DateField()

class Artist(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    hometown = models.CharField(max_length=225)
    date_of_birth = models.DateField()
    is_alive = models.BooleanField(default=False)

class Booking(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    time = models.DateTimeField(default=datetime.today)
    teacher = models.CharField(max_length=225, choices=TEACHERS, default="JW")