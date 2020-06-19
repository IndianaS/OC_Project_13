from django.shortcuts import render


def home(request):
    return render(request, 'collection_pop/home.html')
