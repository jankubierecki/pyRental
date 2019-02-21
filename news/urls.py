from django.urls import path
from .views import home, catalog

urlpatterns = [
    path('', home, name='news-home'),
    path('catalog/', catalog, name='news-catalog'),
]
