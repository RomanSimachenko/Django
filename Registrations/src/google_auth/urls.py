from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('', views.index, name="google-auth"),
]
