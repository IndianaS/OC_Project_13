from django.shortcuts import render


def home(request):
    return render(request, 'collection_pop/home.html')

def legal_notice(request):
    return render(request, 'collection_pop/legal_notice.html')
