from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe, Ingredient

def index(request):
    return HttpResponse('This is a standard message.')

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, 'recipe_list.html', ctx)
def recipe_detail(request, pk):
    currentrecipe = Recipe.objects.get(pk=pk)
    ingredients = Ingredient.objects.filter(recipe__recipe=currentrecipe)
    ctx = {
         "ingredients": ingredients
    }
    return render(request, 'recipe_detail.html', ctx)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'