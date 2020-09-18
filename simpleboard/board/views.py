from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db import models

from .models import Post

def board_list(request):
    posts = Post.objects.all()

    return render(request, 'board_list.html', {'posts': posts})


def board_view(request):
    id=request.GET['id']
    posts=Post.objects.filter(id=id)

    return render(request, "board_view.html", {'posts' : posts})
 

def board_write(request):
    return render(request, "board_write.html")

def board_insert(request):
    post=Post()
    post.title= request.GET['title']
    post.note= request.GET['note']
    post.date= timezone.datetime.now()
    post.save()

    return redirect('/')

def board_update(request):
    id=request.GET['id']
    posts=Post.objects.filter(id=id)

    return render(request, "board_update.html", {'posts' : posts})

def update(request, id):
    posts=Post.objects.filter(id=id)

    if request.method =="POST":
        posts.title=request.POST['title']
        posts.note=request.POST['note']
        posts.date=timezone.datetime.now()
        posts.save()
        return redirect("/")
    else:
        return render(request, 'board_update.html')
