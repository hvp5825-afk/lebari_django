from django.shortcuts import render, get_object_or_404
from .models import Post, BlogCategory
from core.models import SiteSetting
from core.views import get_cms_context
def blog_list(request):
    settings = SiteSetting.objects.first()
    posts = Post.objects.all().order_by('-created_at')
    
    category_slug = request.GET.get('category')
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
        
    query = request.GET.get('q')
    if query:
        posts = posts.filter(title__icontains=query)
        
    categories = BlogCategory.objects.all()
    ctx = {
        'settings': settings,
        'posts': posts,
        'categories': categories,
        'current_category': category_slug,
        'query': query,
    }
    ctx.update(get_cms_context('blog_list'))
    return render(request, 'blog.html', ctx)

def blog_detail(request, slug):
    from .models import Comment
    from django.contrib import messages
    from django.shortcuts import redirect
    
    settings = SiteSetting.objects.first()
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        content = request.POST.get('message')
        if name and email and content:
            Comment.objects.create(post=post, name=name, email=email, content=content)
            messages.success(request, 'Your comment has been posted successfully.')
            return redirect('blog_detail', slug=post.slug)

    comments = post.comments.filter(is_active=True).order_by('-created_at')
    related_posts = Post.objects.exclude(slug=slug).order_by('-created_at')[:3]
    categories = BlogCategory.objects.all()
    ctx = {
        'settings': settings,
        'post': post,
        'comments': comments,
        'related_posts': related_posts,
        'categories': categories,
    }
    ctx.update(get_cms_context('blog_detail'))
    return render(request, 'blog-detail.html', ctx)

from django.shortcuts import redirect
def default_blog_detail(request):
    settings = SiteSetting.objects.first()
    post = Post.objects.first()
    if not post:
        return redirect('blog_list')
    ctx = {'settings': settings, 'post': post}
    ctx.update(get_cms_context('blog_detail'))
    return render(request, 'blog-detail.html', ctx)
