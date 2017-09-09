from django.shortcuts import render


def index(request):
    context = {"test": 15}
    return render(request, 'home/index.html', context)
