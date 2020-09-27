from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomAddFigurineCreationForm, CustomCommentCreationForm
from .models import DidYouSee, Figurine


@login_required(login_url='/users/login/')
def add_figurine(request):
    """Django View add a figurine to his collection"""
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
    """Django View from User Collection"""
    user = request.user
    figurines = user.figurine_set.all()
    return render(
        request, 'figurines/collection.html', {'figurines': figurines}
    )


@login_required(login_url='/users/login/')
def search(request):
    """Django View collection figurine finder"""
    user = request.user

    if request.method == 'GET':
        if request.GET.get('all'):
            figurines_list = user.figurine_set.all()
        else:
            query = request.GET['q']
            figurines_list = user.figurine_set.filter(name__icontains=query)
    else:
        redirect('/figurines/collection/')
    return render(
        request, 'figurines/search.html', {'figurines_list': figurines_list}
    )


@login_required(login_url='/users/login/')
def did_you_see(request):
    """Django View of the section that viewed"""
    questions = [
        post for post in DidYouSee.objects.all() if post.id == post.parent.id
    ]
    return render(
        request, 'figurines/did_you_see.html', {'questions': questions}
    )


@login_required(login_url='/users/login/')
def post_detail(request, id_post):
    """Django View response to a figurine search"""
    main_post = get_object_or_404(DidYouSee, id=id_post)
    responses = DidYouSee.objects.filter(parent=main_post).exclude(
        id=main_post.id
    )

    context = {
        'main_post': main_post,
        'responses': responses,
    }

    return render(request, 'figurines/post_detail.html', context)


@login_required(login_url='/users/login/')
def create_question(request, id_post=None):
    """Django View for creating a question"""
    if request.method == 'POST':
        form = CustomCommentCreationForm(request.POST)
        if form.is_valid():
            annonce = form.save(commit=False)
            annonce.author = request.user
            annonce.save()

            if id_post:
                post = get_object_or_404(DidYouSee, id=id_post)
                annonce.parent = post
                mail_user = annonce.parent.author.email
                mail = EmailMessage(
                    "Bonjour !",
                    "Une Réponse a été posté sur votre commentaire de recherche !",
                    to=[mail_user],
                )
                mail.send()

            else:
                annonce.parent = annonce

            annonce.save()

            return redirect('/figurines/did_you_see/')
    else:
        form = CustomCommentCreationForm()
    return render(request, 'figurines/create_question.html', {'form': form})


@login_required(login_url='/users/login/')
def delete_figurine(request):
    """Django deletion view of a figurine"""
    if request.method == 'POST':
        user = request.user
        id_figurine = request.POST.get("id_figurine")
        figurine = Figurine.objects.get(id=id_figurine)
        figurine.delete()
        return redirect('/figurines/collection/')


def report(request, id_post):
    """Django seen from a post"""
    post = get_object_or_404(DidYouSee, id=id_post)
    post.report = True
    post.save()
    mail = EmailMessage(
        "Urgent !", "Un post a été signalé !", to=['benjamin.rejaud@gmail.com']
    )
    mail.send()
    return render(request, 'figurines/report.html')
