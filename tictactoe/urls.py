from django.urls import path
from . import views

urlpatterns = [
    path("", views.tictactoe, name="tictactoe"),
    path("square-click/", views.square_click, name="square-click"),
]
