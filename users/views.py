from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse
from figurines.models import Figurine
from friendship.exceptions import AlreadyExistsError, AlreadyFriendsError
from friendship.models import Friend, FriendshipRequest

from users.models import User

from .forms import CustomUserCreationForm


@login_required(login_url='/users/login/')
def profile(request):
    """Django view profile page"""
    return render(request, 'users/profile.html')


def create_account(request):
    """Django view account creation"""
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
    """Django view del user"""

    if not request.user.is_superuser:
        username = request.user
        user = User.objects.get(username=username)
        user.delete()

    return redirect('/')


@login_required(login_url='/users/login/')
def friends_list(request):
    """Django view friends list page"""
    friends = Friend.objects.friends(request.user)
    friend_requests = Friend.objects.unrejected_requests(user=request.user)
    friend_request_pending = [
        User.objects.get(pk=friend.from_user_id) for friend in friend_requests
    ]

    try:
        user_found = request.session['user_found']
        del request.session['user_found']
    except KeyError:
        user_found = None

    try:
        user_not_found = request.session['user_not_found']
        del request.session['user_not_found']
    except KeyError:
        user_not_found = None
    
    try:
        user_already_added = request.session['user_already_added']
        del request.session['user_already_added']
    except KeyError:
        user_already_added = None

    context = {
        'friends': friends,
        'friend_requests': friend_requests,
        'friend_request_pending': friend_request_pending,
        'user_not_found': user_not_found,
        'user_found': user_found,
        'user_already_added': user_already_added,
    }

    return render(request, 'users/friends_list.html', context)


@login_required(login_url='/users/login/')
def add_friend(request):
    """Django view add friend"""
    try:
        username = request.POST['username']
        other_user = User.objects.get(username=username)
        add_friend = Friend.objects.add_friend(request.user, other_user)
        request.session[
            'user_found'
            ] = f"Demande d'amis envoyée !"

    except User.DoesNotExist:
        request.session[
            'user_not_found'
        ] = f'Utilisateur "{username}" inconnu.'
        return redirect(reverse('users:friends_list'))
    
    except AlreadyExistsError:
        request.session[
            'user_already_added'
            ] = f"La demande à déjà été envoyée !"
    
    except AlreadyFriendsError:
        request.session[
            'user_already_added'
            ] = f"La demande à déjà été envoyée !"

    return redirect('/users/friends_list/')


@login_required(login_url='/users/login/')
def accept_request(request):
    """Django view accept request add friend"""
    user = request.user
    other_user_id = request.POST.get('other_user_id')
    friend_request = FriendshipRequest.objects.get(
        from_user=other_user_id, to_user=user.id
    )

    user_choice = request.POST.get('user_choice')

    if user_choice == "Accepted":
        friend_request.accept()
    else:
        friend_request.reject()
        friend_request.delete()

    return redirect('/users/friends_list/')


@login_required(login_url='/users/login/')
def remove_friend(request):
    """Django view remove friend the friend list"""
    user = request.user
    other_user_id = request.POST.get('other_user_id')

    other_user = get_object_or_404(User, id=other_user_id)
    user_del = Friend.objects.remove_friend(request.user, other_user)

    return redirect('/users/friends_list/')


@login_required(login_url='/users/login/')
def friends_figurine(request, id):
    friend = get_object_or_404(User, id=id)
    return render(request, 'users/friends_figurine.html', {'friend': friend})


@login_required(login_url='/users/login/')
def friends_figurine_search(request):
    id = request.GET['friend_id']
    friends_selected = User.objects.get(id=id)

    if Friend.objects.are_friends(request.user, friends_selected):
        if request.GET.get('q'):
            query = request.GET['q']
            figurines_list = friends_selected.figurine_set.filter(name__icontains=query)
        elif request.GET.get('all'):
            figurines_list = friends_selected.figurine_set.all()          
        else:
            return redirect('/users/friends_list/')

        return render(
            request,
            'users/friends_figurine_search.html',
            {'figurines_list': figurines_list}
        )

    else:
        return redirect('/users/friends_list/')
