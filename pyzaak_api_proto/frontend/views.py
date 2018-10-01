from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers

from api.models import Profile, SideDeck
from .forms import SignUpForm, EditProfileForm


def home(request):
    return render(request, 'frontend/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'frontend/signup.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    deck = serializers.serialize("python",
                                 [SideDeck.objects.get(user=user)])[0]
    context = {'user': user,
               'profile': profile,
               'deck': deck}
    return render(request, 'frontend/profile.html', context)


@login_required
def edit_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == 'PUT':
        form = EditProfileForm(request.PUT)
        if form.is_valid():
            profile.image = form.cleaned_data.pop('image')
            profile.location = form.cleaned_data.pop('location')
            profile.save()
            form.save()
            return redirect('profile')

    deck = serializers.serialize("python",
                                 [SideDeck.objects.get(user=user)])[0]
    context = {'user': user,
               'profile': profile}
    return render(request, 'frontend/edit_profile.html', context)
