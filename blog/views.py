from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger






def index(request):
    blogs = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(blogs, 4)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request,'blog1/index.html',context={'blogs':blogs})


def detail(request, post_id):
    post = Blog.objects.get(id = post_id)
    return render(request, 'blog1/detail.html', {"post": post})




def addpost(request):
    form = BlogForm
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('index')
    else:
        form = BlogForm()
    return render(request, 'blog1/addpost.html', context={'form': form})

def search_post(request):
    query = request.GET.get('query')
    data = Blog.objects.filter(
        Q(title__icontains=query) |
        Q(text__icontains=query)
    )
    return render(request, 'blog1/search.html', {'data': data})


def edit_post(request, post_id):
    post = Blog.objects.get(pk=post_id)
    form = BlogForm(instance=post)

    if request.user != post.author:
        return HttpResponse("Siz buni o'zgartira olmaysiz")

    if request.method == "POST":
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "blog1/editpost.html", {"form": form})



def logoutUser(request):
    logout(request)
    return redirect('index')


@login_required(login_url="login")
def delete_post(request, post_id):
    post = Blog.objects.get(pk=post_id)
    if request.user != post.author:
        return HttpResponse("Siz buni o'chira olmaysiz")
    else:
        post.delete()
        return redirect('index')

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)

            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'blog1/login.html')


