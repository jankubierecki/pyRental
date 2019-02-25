from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import generics, permissions

from rentals.forms import RentalCreateForm
from rentals.models import Rental
from rentals.permissions import IsOwnerOrReadOnly
from rentals.serializers import RentalSerializer
from vehicles.models import Car


class RentalListView(ListView):
    model = Rental
    template_name = 'rentals/rental_list.html'
    context_object_name = 'rental'


class RentalDetailView(DetailView):
    model = Rental
    template_name = 'rentals/rental_details.html'
    context_object_name = 'rental'


class RentalListAPI(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class RentalDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class RentalCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = RentalCreateForm
    template_name = 'rentals/rental_create.html'
    success_message = 'Created'
    context_object_name = 'order'

    def get_success_url(self):
        return reverse('rental-detail', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        kwargs = super(RentalCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user, 'car': self.kwargs['pk']})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = get_object_or_404(Car, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile

        car = Car.objects.get(pk=self.kwargs['pk'])
        form.instance.car = car

        return super().form_valid(form)
