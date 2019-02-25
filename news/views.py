from django.shortcuts import render
from django.views.generic import ListView, DetailView

from news.models import Post
from vehicles.models import Car


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-created_at')[:3],
        'title': 'Welcome!'
    }
    return render(request, 'news/home.html', context)


class CatalogListView(ListView):
    model = Car
    template_name = 'news/catalog.html'
    context_object_name = 'cars'
    ordering = ['name']


class CarDetailView(DetailView):
    model = Car
    template_name = 'news/car_details.html'
    context_object_name = 'car'
