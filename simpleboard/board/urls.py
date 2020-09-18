from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('board_write', views.board_write, name="board_write"),
    path('board_view', views.board_view, name="board_view"),
    path('board_insert',views.board_insert, name="board_insert"),
    path('board_update',views.board_update, name="board_update"),
    path('update',views.update, name="update"),
    path('board_delete',views.board_delete, name="board_delete"),
]