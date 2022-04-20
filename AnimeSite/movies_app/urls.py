from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage, name="index"),
    path("player/<str:pk>/", views.PlayerView, name="player"),
    path('<str:pk>/', views.DetailMovieView, name="movie_detail"),
]
