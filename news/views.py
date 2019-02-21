from django.shortcuts import render

from news.models import Post
from vehicles.models import Car


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-created_at')[:3],
        'title': 'Welcome!'
    }
    return render(request, 'news/home.html', context)


def catalog(request):
    context = {
        'cars': Car.objects.all().order_by('-name'),
        'title': 'Oferta'
    }
    return render(request, 'news/catalog.html', context)
