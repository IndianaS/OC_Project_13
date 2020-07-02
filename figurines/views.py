from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CustomAddFigurineCreationForm


@login_required(login_url='/users/login/')
def add_figurine(request):
    user = request.user
    if request.method == 'POST':
        form = CustomAddFigurineCreationForm(request.POST, request.FILES)
        if form.is_valid():
            figurine = form.save()
            figurine.user.add(user)

            return redirect('/users/collection')
    else:
        form = CustomAddFigurineCreationForm()
    return render(request, 'figurines/add_figurine.html', {'form': form})
