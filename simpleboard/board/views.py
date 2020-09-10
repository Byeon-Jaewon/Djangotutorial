from django.shortcuts import render
from django.utils import timezone
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