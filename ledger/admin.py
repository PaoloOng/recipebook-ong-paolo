from django.contrib import admin

from .models import Recipe, Ingredient, RecipeIngredient

class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    inlines = [RecipeIngredientInLine]

admin.site.register(Recipe, RecipeAdmin)
