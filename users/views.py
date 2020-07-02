from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, CustomCommentCreationForm
from figurines.models import Figurine


@login_required(login_url='/users/login/')
def profile(request):
    """Django view profile page."""
    return render(request, 'users/profile.html')


def create_account(request):
    """Django view account creation."""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/users/profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/create_account.html', {'form': form})


@login_required(login_url='/users/login/')
def collection_user(request):
    user = request.user
    result = None
    try:
        query = request.GET['q']
        figurines_list = user.figurine_set.filter(name__icontains=query)
    except KeyError:
        print('Pas de requête')
    return render(request, 'figurines/result_search.html', {'figurines_list': figurines_list})


@login_required(login_url='/users/login/')
def did_you_see(request):
    if request.method == 'POST':
        form = CustomCommentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/did_you_see')
    else:
        form = CustomCommentCreationForm()
    return render(request, 'users/did_you_see.html', {'form': form})
