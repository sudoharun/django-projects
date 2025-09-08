from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

class Recipe(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    ingredients = models.TextField()
    recipe = models.TextField()
    gluten_free = models.BooleanField()
    image_link = models.CharField(max_length=225, default='images/placeholder_cake.jpg')

    def __str__(self):
        return self.name

class Cake(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class User(AbstractUser):
    cakes = MultiSelectField(
        choices=[(cake.id, cake.name) for cake in Cake.objects.all()],
        null=True,
    )
    recipes = MultiSelectField(
        choices=[(recipe.id, recipe.name) for recipe in Recipe.objects.all()],
        null=True,
    )
    pass
