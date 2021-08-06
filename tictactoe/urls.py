from django.urls import path
from . import views

urlpatterns = [
    path("", views.tictactoe, name="tictactoe"),
    path("square-click/", views.square_click, name="square-click"),
    path("change-first/", views.change_first, name="change-first"),
    path("new-game/", views.new_game, name="new-game"),
]
