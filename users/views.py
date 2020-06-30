from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, CustomAddFigurineCreationForm
from figurines.models import Collection


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
    figurine_collection = Collection.objects.filter(user=user)
    return render(request, 'users/collection.html')


@login_required(login_url='/users/login/')
def did_you_see(request):
    return render(request, 'users/did_you_see.html')


@login_required(login_url='/users/login/')
def add_figurine(request):
    if request.method == 'POST':
        form = CustomAddFigurineCreationForm(request.POST)
        if form.is_valid():
            form.save()
            id = form.cleaned_data.get('id')
            category = form.cleaned_data.get('category')
            name = form.cleaned_data.get('name')
            picture_figurine = form.cleaned.get('picture_figurine')
            return redirect('/users/collection')
    else:
        form = CustomAddFigurineCreationForm()
    return render(request, 'users/add_figurine.html', {'form': form})
