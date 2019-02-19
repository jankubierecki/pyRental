from django.shortcuts import render

from news.models import Post


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-created_at')[:3],
        'title': 'Welcome!'
    }
    return render(request, 'news/home.html', context)
