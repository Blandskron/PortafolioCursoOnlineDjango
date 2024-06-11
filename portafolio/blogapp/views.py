from django.shortcuts import render
from .models import Blog

def listadeblog(request):
    blogs = Blog.objects.all()
    return render(request, 'blogapp/blog.html', {'blogs': blogs})

def detalledeblog(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blogapp/blog_detail.html', {'blog': blog})