from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.filter(status='published').order_by('-published_date')[:3]
    return render(request, 'app/home.html', {'posts': posts})

def about(request):
    return render(request, 'app/about.html')

def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-published_date')
    return render(request, 'app/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, status='published')
    return render(request, 'app/post_detail.html', {'post': post})
