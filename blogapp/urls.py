from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.blog_list, name='blog'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
]