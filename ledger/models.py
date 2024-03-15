from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    #after doing a quick lookup I found that there is a (fictional) Greek dish/recipe
    #consisting of 171 letters, so just in case I set this to 200 letters
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50, null=True)
    createdon = models.DateTimeField(auto_now_add=True, null=True)
    updateon = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100, null=True)
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
        related_name="recipe"
    )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        related_name="ingredients"
    )
