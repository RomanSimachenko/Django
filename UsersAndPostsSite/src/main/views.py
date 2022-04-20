from django.shortcuts import redirect, render
from src.users.forms import CustomUserCreationForm, UploadAvatar
from src.users.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from . import models
from . import forms
from django.db.models import Q


def IndexView(request):
    q = request.GET.get('q', None)
    context = {
        "posts": models.Post.objects.filter(
            Q(title__icontains=q) |
            Q(description__icontains=q) |
            Q(short_description__icontains=q)
        ) if q else models.Post.objects.all(),
    }
    if request.user.is_authenticated:
        context['liked'] = models.Post.objects.filter(
            user=request.user).filter(liked=request.user)
    return render(request, "main/index.html", context=context)


def UsersView(request):
    q = request.GET.get('q', None)
    context = {
        "users": CustomUser.objects.filter(username__icontains=q) if q else CustomUser.objects.all(),
    }
    if request.user.is_authenticated:
        try:
            context["followed"] = models.Follower.objects.get(
                user=request.user).followers.all()
        except ObjectDoesNotExist:
            context["followed"] = []
    return render(request, "main/users.html", context=context)


def LoginView(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username, password = request.POST.get(
            'username'), request.POST.get('password')
        try:
            user = CustomUser.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "User doesn't exist")
            return redirect('login')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Password is incorrect")
            return redirect('login')

    return render(request, "main/login.html")


def RegisterView(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        messages.error(request, "Form is invalid")
        return redirect('register')

    return render(request, "main/register.html")


def LogoutView(request):
    logout(request)
    return redirect('index')


def PostView(request, pk):
    try:
        post = models.Post.objects.get(id=pk)
    except ObjectDoesNotExist:
        return render(request, "main/404.html")

    if request.method == 'POST':
        form = forms.AddCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.save()
            post.comments.add(new_comment)
            return redirect('post', pk)

    context = {
        "comments": post.comments.all(),
        "post": post,
        "liked": post.liked.all(),
        "form": forms.AddCommentForm(),
    }
    return render(request, "main/post.html", context=context)


def PostCreateView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = forms.CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('index')
    context = {
        "form": forms.CreatePostForm(),
    }
    return render(request, "main/create-post.html", context=context)


def PostDeleteView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        post = models.Post.objects.get(id=pk)
        if request.user == post.user:
            post.delete()
            return redirect('index')
    except ObjectDoesNotExist:
        pass
    return redirect('post', pk)


def ProfileView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    try:
        user = CustomUser.objects.get(id=pk)
    except ObjectDoesNotExist:
        return render(request, "main/404.html")

    if request.POST:
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        avatar = request.FILES.get('avatar', None)
        user.avatar = avatar if avatar else user.avatar
        user.save()
        return redirect('profile', pk)

    context = {
        "user": user,
        "form": UploadAvatar(),
        "folls": models.Follower.objects.get_or_create(user=request.user)[0].followers.all(),
        "posts": models.Post.objects.filter(user__id=pk),
        "followers": models.Follower.objects.filter(followers=user),
    }
    return render(request, "main/profile.html", context=context)


def FollowView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    try:
        if request.user == models.CustomUser.objects.get(id=pk):
            return redirect('profile', pk)
        f = models.Follower.objects.get_or_create(user=request.user)[0]
        f.followers.add(models.CustomUser.objects.get(id=pk))
    except:
        pass
    return redirect('profile', pk)


def UnfollowView(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    try:
        if request.user == models.CustomUser.objects.get(id=pk):
            return redirect('profile', pk)
        f = models.Follower.objects.get(user=request.user)
        f.followers.remove(models.CustomUser.objects.get(id=pk))
    except ObjectDoesNotExist:
        pass
    return redirect('profile', pk)


def LikeView(request, pk):
    if not request.user.is_authenticated:
        return redirect('index')
    try:
        post = models.Post.objects.get(id=pk)
    except ObjectDoesNotExist:
        return redirect('error')
    post.liked.add(request.user)
    return redirect('post', pk)


def DislikeView(request, pk):
    if not request.user.is_authenticated:
        return redirect('index')
    try:
        post = models.Post.objects.get(id=pk)
    except ObjectDoesNotExist:
        return redirect('error')
    post.liked.remove(request.user)
    return redirect('post', pk)


def UncommentView(request, pk, pk2):
    if not request.user.is_authenticated:
        return redirect('index')
    try:
        post = models.Post.objects.get(id=pk)
    except ObjectDoesNotExist:
        return redirect('error')
    try:
        comment = models.Comment.objects.get(id=pk2)
    except ObjectDoesNotExist:
        return redirect('error')
    if post.user == comment.user:
        post.comments.remove(comment)
    else:
        return redirect('error')
    return redirect('post', pk)
