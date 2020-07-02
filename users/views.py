from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, CustomAddFigurineCreationForm, CustomCommentCreationForm
from figurines.models import Collection, Figurine


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
    # figurine_collection = Collection.objects.get(user=user)
    result = None
    # try:
    #     figurine_search = request.GET['q']
    #     figurine = Figurine.objects.filter(name__icontains=figurine_search)
    #     if figurine:
    #         collection_figurine = figurine.figurines()
    #     else:
    #         collection_figurine = None

    # except KeyError:
    #     print('Pas de requête')
    """
    try:
        query = request.GET['q']
        figurines = Figurine.objects.filter(name__icontains=query)
    except KeyError:
        print('Pas de requête')
    """

    return render(request, 'users/collection.html',)

@login_required(login_url='/users/login/')
def did_you_see(request):
    if request.method == 'POST':
        form = CustomCommentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            text = form.cleaned_data.get('text')
            data = form.cleaned_data.get('data')
            return redirect('/users/did_you_see')
    else:
        form = CustomCommentCreationForm()
    return render(request, 'users/did_you_see.html', {'form': form})


@login_required(login_url='/users/login/')
def add_figurine(request):
    user = request.user
    if request.method == 'POST':
        form = CustomAddFigurineCreationForm(request.POST, request.FILES)
        if form.is_valid():
            figurine = form.save()
            user_collection, created = Collection.objects.get_or_create(user=user, figurine=figurine)
            if not created:
                status = "Déjà ajouté à la collection"

            return redirect('/users/collection')
    else:
        form = CustomAddFigurineCreationForm()
    return render(request, 'users/add_figurine.html', {'form': form})
