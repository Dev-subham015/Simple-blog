from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post_details(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'post_details.html', {'post': post})
