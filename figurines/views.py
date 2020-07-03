from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CustomAddFigurineCreationForm, CustomCommentCreationForm
from .models import DidYouSee, Figurine

@login_required(login_url='/users/login/')
def add_figurine(request):
    user = request.user
    if request.method == 'POST':
        form = CustomAddFigurineCreationForm(request.POST, request.FILES)
        if form.is_valid():
            figurine = form.save()
            figurine.user.add(user)

            return redirect('/figurines/collection')
    else:
        form = CustomAddFigurineCreationForm()
    return render(request, 'figurines/add_figurine.html', {'form': form})


@login_required(login_url='/users/login/')
def collection_user(request):
    user = request.user
    figurines = user.figurine_set.all()
    return render(request, 'figurines/collection.html', {'figurines': figurines})


@login_required(login_url='/users/login/')
def search(request):
    user = request.user

    if request.method == 'GET':
        query = request.GET['q']
        figurines_list = user.figurine_set.filter(name__icontains=query)
    else:
        print('Pas de requête')
        redirect('/figurines/collection/')
    return render(request, 'figurines/search.html', {'figurines_list': figurines_list})


@login_required(login_url='/users/login/')
def did_you_see(request):
    questions = DidYouSee.objects.all()
    return render(request, 'figurines/did_you_see.html', {'questions': questions})

@login_required(login_url='/users/login/')
def create_question(request):
    if request.method == 'POST':
        form = CustomCommentCreationForm(request.POST)
        if form.is_valid():
            annonce = form.save(commit=False)
            annonce.author = request.user
            annonce.save()

            return redirect('/figurines/did_you_see/')
    else:
        form = CustomCommentCreationForm()
    return render(request, 'figurines/create_question.html', {'form': form})


@login_required(login_url='/users/login/')
def delete_figurine(request):
    if request.method == 'POST':
        user = request.user
        id_figurine = request.POST.get("id_figurine")
        print(id_figurine)
        figurine = Figurine.objects.get(id=id_figurine)
        figurine.delete()
        return redirect('/figurines/collection/')
