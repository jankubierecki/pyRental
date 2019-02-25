from django.urls import path
from .views import RentalDetailView, RentalListView, RentalCreateView

urlpatterns = [
    path('', RentalListView.as_view(), name='rental-list'),
    path('<int:pk>/', RentalDetailView.as_view(), name='rental-detail'),
    path('new/<int:pk>/', RentalCreateView.as_view(), name='rental-create'),
]
