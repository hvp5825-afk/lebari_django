from django.shortcuts import render, get_object_or_404
from .models import Post, BlogCategory
from core.models import SiteSetting

def blog_list(request):
    settings = SiteSetting.objects.first()
    posts = Post.objects.all().order_by('-created_at')
    categories = BlogCategory.objects.all()
    return render(request, 'blog-list.html', {
        'settings': settings,
        'posts': posts,
        'categories': categories,
    })

def blog_detail(request, slug):
    settings = SiteSetting.objects.first()
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog-detail.html', {
        'settings': settings,
        'post': post,
    })

from django.shortcuts import redirect
def default_blog_detail(request):
    settings = SiteSetting.objects.first()
    post = Post.objects.first()
    if not post:
        return redirect('blog_list')
    return render(request, 'blog-detail.html', {'settings': settings, 'post': post})
