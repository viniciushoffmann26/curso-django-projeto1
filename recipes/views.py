from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contato(request):
    return HttpResponse('Contato')


def sobre(request):
    return HttpResponse('Sobre')
