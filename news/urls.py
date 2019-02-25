from django.urls import path
from .views import home, CatalogListView, CarDetailView

urlpatterns = [
    path('', home, name='news-home'),
    path('catalog/', CatalogListView.as_view(), name='news-catalog'),
    path('catalog/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
]
