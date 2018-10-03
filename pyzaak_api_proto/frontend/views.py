from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.core import serializers

from api.models import Profile, SideDeck, Game
from .models import BlogPost
from .forms import SignUpForm


def home(request):
    games = Game.objects.all().order_by('-finished_at')
    try:
        post = BlogPost.objects.latest('date_added')
    except DoesNotExist:
        post = {title: 'No Posts',
                body: 'Add a post!',
                created_by: '',
                date_added: None}
    return render(request, 'frontend/home.html', {'games': games, 'post': post})


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


# @login_required
# def edit_profile(request):
#     user = request.user
#     profile = Profile.objects.get(user=user)
#     if request.method == 'POST':
#         if request.FILES['image']:
#             image = request.FILES['imge']
#             fs = FileSystemStorage()
#             filename = fs.save(myfile.name, myfile)
#             uploaded_file_url = fs.url(filename)
#         profile.image = form.cleaned_data.pop('image')
#         profile.location = form.cleaned_data.pop('location')
#         profile.save()
#         form.save()
#         return redirect('profile')

#     deck = serializers.serialize("python",
#                                  [SideDeck.objects.get(user=user)])[0]
#     context = {'user': user,
#                'profile': profile}
#     return render(request, 'frontend/edit_profile.html', context)
