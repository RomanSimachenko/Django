from django.urls import path
from . import views

urlpatterns = [
    path('quiz/<int:pk>/', views.QuizView, name="quiz"),
    # path('', views.IndexPage, name="index"),
]
