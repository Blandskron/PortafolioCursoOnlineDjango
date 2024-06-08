from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.listadeblog, name='blog'),
    path('<int:pk>/', views.detalledeblog, name='blog_detail'),
]