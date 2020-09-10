from django.shortcuts import render
from django.utils import timezone
from .models import Post

def board_list(request):
    posts = Post.objects.all()

    return render(request, 'board/board_list.html', {'posts': posts})

def board_write(request):
    return render(request, "board/board_write.html", )

def board_insert(request):
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    date = date.today()

    if btitle != "":
        rows = Post.objects.create(b_title=btitle, b_note=bnote, date=bdate)
        return redirect('/board_list')
    else:
        return redirect('/board_write')