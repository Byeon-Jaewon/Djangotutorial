from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list, name='board_list'),
#    path('board_write', views.board_write, name="board_write"),
]