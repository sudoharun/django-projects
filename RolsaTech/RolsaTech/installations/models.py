from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

class Installation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    date = models.DateField()
    postcode = models.CharField(max_length=8, default='')
    city = models.CharField(max_length=16, default='')
    county = models.CharField(max_length=32, default='')
    first_line = models.CharField(max_length=64, default='')

    def __str__(self):
        return f'Installation #{self.id}'
