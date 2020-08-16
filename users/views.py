from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from friendship.models import Friend, Follow, Block

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
        return redirect('/users/profile/')

    return redirect('/')


@login_required(login_url='/users/login/')
def friends_list(request):
    """Django view friends list page."""
    friends = Friend.objects.friends(request.user)
    friend_requests = Friend.objects.unrejected_requests(user=request.user)
    friend_request_test = [ User.objects.get(pk=friend.from_user_id) for friend in friend_requests]

    context = {
        'friends': friends,
        'friend_requests': friend_requests,
        'friend_request_test': friend_request_test,

        }

    return render(request, 'users/friends_list.html', context)


@login_required(login_url='/users/login/')
def add_friend(request):
    username = request.POST['username']
    other_user = get_object_or_404(User, username=username)
    add_friend = Friend.objects.add_friend(
        request.user,
        other_user
        )
    
    return redirect('/users/friends_list/')
