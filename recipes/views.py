from django.shortcuts import render


# Create your views here.
def home(request):
    name = 'victor'
    
    return render(request, 'recipes/home.html', context={
        'name': name,
    })
