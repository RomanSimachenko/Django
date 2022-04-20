from django.urls import path, include
from . import views

urlpatterns = [
    path('social-auth/', include('social_django.urls', namespace="social")),

    path('', views.IndexView, name="index"),

    path('register/', views.RegisterView, name="register"),
    path('', include('django.contrib.auth.urls')),

    path('verify_email/complete/', views.VerifyEmailCompleteView,
         name="verify_email_complete"),
    path('verify_email/<str:uid>/<str:email>/',
         views.VerifyEmailView, name="verify_email"),
    path('verify_email/done/', views.VerifyEmailDoneView,
         name="verify_email_done"),

    path('profile/<int:pk>/', views.ProfileView, name="user-profile"),
]
