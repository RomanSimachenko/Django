from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),

    path('register/', views.RegisterView, name="register"),
    path('login/', views.LoginView, name="login"),
    path('logout/', views.LogoutView, name='logout'),

    path('google-auth/', include('src.google_auth.urls')),

    path('user-profile/<int:id>/', views.UserProfileView, name="user-profile"),

    path("verify-email/<str:data1>/<str:data2>/",
         views.VerifyEmailView, name="verify-email"),
]
