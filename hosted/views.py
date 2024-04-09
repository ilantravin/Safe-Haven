from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group


# Create your views here.

from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            category = form.cleaned_data.get('category')
            if category == 'host':
                group = Group.objects.get(name='מארח')  # replace 'host' with the actual group name for hosts
                user.groups.add(group)
            elif category == 'hosted':
                group = Group.objects.get(name='מתארח')  # replace 'מתארח' with the actual group name for hosted users
                user.groups.add(group)
            login(request, user)
            return redirect('homepage')
    else:
        form = CustomUserCreationForm()

    return render(request, 'hosted/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
    else:
        form = AuthenticationForm()

    return render(request, 'hosted/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
