from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={'nome': 'Vinicius Hoffmann'})


def contato(request):
    return render(request, 'me-apague/temp.html')


def sobre(request):
    return render(request, 'global/home.html')
