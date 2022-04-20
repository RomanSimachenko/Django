from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView, name='index'),

    path('users/', views.UsersView, name="users"),

    path("login/", views.LoginView, name="login"),
    path("register/", views.RegisterView, name="register"),
    path("logout/", views.LogoutView, name="logout"),

    path('post/<int:pk>/', views.PostView, name="post"),
    path('post/create/', views.PostCreateView, name='create-post'),
    path('post/delete/<int:pk>/', views.PostDeleteView, name='delete-post'),

    path("profile/<int:pk>/", views.ProfileView, name="profile"),
    path('follow/<int:pk>/', views.FollowView, name="follow"),
    path('unfollow/<int:pk>/', views.UnfollowView, name="unfollow"),

    path('like/<int:pk>/', views.LikeView, name="like"),
    path('dislike/<int:pk>/', views.DislikeView, name="dislike"),

    path('uncomment/<int:pk>/<int:pk2>/',
         views.UncommentView, name="uncomment"),
]
