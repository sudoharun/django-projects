from django.db import models
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=64, unique=True)
    image = models.ImageField(default='images/fallback.png', upload_to='images/')
    description = models.TextField(blank=True)
    installation_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
