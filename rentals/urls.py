from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import RentalDetailView, RentalListView, RentalCreateView, RentalDetailAPI, RentalListAPI
from users.views import UserDetail, UserList

urlpatterns = [
    # path('', RentalListView.as_view(), name='rental-list'),
    # path('<int:pk>/', RentalDetailView.as_view(), name='rental-detail'),
    path('', RentalListAPI.as_view(), name='rental-list'),
    path('<int:pk>', RentalDetailAPI.as_view(), name='rental-detail'),
    path('new/<int:pk>', RentalCreateView.as_view(), name='rental-create'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserList.as_view(), name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
