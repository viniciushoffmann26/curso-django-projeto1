from django.shortcuts import render

from utils.recipes.factory import make_recipe

from .models import Recipes


def home(request):
    recipes = Recipes.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
