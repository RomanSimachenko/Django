from django.urls import path
from . import views

urlpatterns = [
    path('', views.ManageItemsView, name="manage-items"),
    path('<slug:key>/', views.ManageItemView, name="manage-item"),
]
