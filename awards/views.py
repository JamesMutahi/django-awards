from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

# Create your views here.
def index(request):
    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login/')
def profile(request):
    profiles = Profile.objects.all()
    return render(request, 'profile.html', locals())


@login_required(login_url='/accounts/login/')
def edit(request):
    if request.method == 'POST':
        print(request.FILES)
        new_profile = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if new_profile.is_valid():
            new_profile.save()
            print(new_profile.fields)
            # print(new_profile.fields.profile_picture)
            return redirect('profile')
    else:
        new_profile = ProfileForm(instance=request.user.profile)
    return render(request, 'edit.html', locals())
