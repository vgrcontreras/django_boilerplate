from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    name = 'victor'
    
    return render(request, 'recipes/home.html', context={
        'name': name,
    })


def sobre(request):
    return HttpResponse('SOBRE')


def contato(request):
    return HttpResponse('CONTATO')