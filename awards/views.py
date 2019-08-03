from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Post
from .forms import ProfileForm, NewPostForm
from django.contrib.auth.models import User


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


@login_required(login_url='/accounts/login/')
def project(request):
    posts = Post.objects.all().order_by('-post_date')
    return render(request, 'projects.html', locals())


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('project')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})


@login_required(login_url='/accounts/login/')
def user(request, user_id):
    user_object = get_object_or_404(User, pk=user_id)
    if request.user == user_object:
        return redirect('profile')
    user_images = user_object.posts.all()
    return render(request, 'user.html', locals())
