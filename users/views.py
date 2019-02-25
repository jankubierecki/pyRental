from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import generics

from users.models import Profile
from users.serializers import UserSerializer
from .forms import UserRegisterForm


class UserList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rejestracja przebiegła pomyślnie')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    context = {
        'user': Profile.objects.get(user=request.user)
    }
    return render(request, 'users/profile.html', context)
