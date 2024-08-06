from django.shortcuts import render
from .models import Post 

def index_v(request):
    return render(request, 'index.html')

def about_v(request):
    return render(request, 'about.html')

def blog_list(request):
    blogs = Post.objects.all() 
    return render(request, 'about.html', {'posts': blogs})  
