from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoutesView),
    path('products/', views.ProductsView),
    path('product/<int:pk>/', views.getProductView),
]
