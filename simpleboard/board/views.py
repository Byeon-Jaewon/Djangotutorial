from django.shortcuts import render
from django.utils import timezone
from .models import Post

def board_list(request):
    posts = Post.objects.all()

    return render(request, 'board_list.html', {'posts': posts})