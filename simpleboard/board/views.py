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
