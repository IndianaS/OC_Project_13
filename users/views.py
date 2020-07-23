from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from friendship.models import Friend, Follow, Block
from django.contrib.auth.models import User

from figurines.models import Figurine
from users.models import User
from .forms import CustomUserCreationForm


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
def del_user(request):
    """Django view del user."""
    try:
        if not request.user.is_superuser:
            username = request.user
            user = User.objects.get(username=username)
            user.delete()
        
    except User.DoesNotExist:
        return redirect('/users/profile')

    return redirect('/')


@login_required(login_url='/users/login/')
def friends_list(request):
    """Django view friends list page."""
    return render(request, 'users/friends_list.html')
