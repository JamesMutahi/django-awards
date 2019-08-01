from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html', locals())


def profile(request):
    return render(request, 'profile.html', locals())


