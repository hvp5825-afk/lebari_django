import os
import re

def update_file(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    base_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django"
    
    # 1. Update blog/views.py
    views_path = os.path.join(base_dir, 'blog', 'views.py')
    with open(views_path, 'r', encoding='utf-8') as f:
        v_content = f.read()
    if 'def default_blog_detail' not in v_content:
        v_content += "\nfrom django.shortcuts import redirect\ndef default_blog_detail(request):\n    settings = SiteSetting.objects.first()\n    post = Post.objects.first()\n    if not post:\n        return redirect('blog_list')\n    return render(request, 'blog-detail.html', {'settings': settings, 'post': post})\n"
        with open(views_path, 'w', encoding='utf-8') as f:
            f.write(v_content)
            
    # 2. Update blog/urls.py
    urls_path = os.path.join(base_dir, 'blog', 'urls.py')
    update_file(urls_path, [
        ("path('', views.blog_list, name='blog_list'),", "path('', views.blog_list, name='blog_list'),\n    path('detail/', views.default_blog_detail, name='default_blog_detail'),")
    ])
    
    # 3. Update base.html menu link
    base_html = os.path.join(base_dir, 'templates', 'base.html')
    update_file(base_html, [
        ('<li><a href="{% url \'blog_list\' %}">Blog Detail</a></li>', '<li><a href="{% url \'default_blog_detail\' %}">Blog Detail</a></li>')
    ])
    
    # 4. Make blog-list.html dynamic
    blog_list_path = os.path.join(base_dir, 'templates', 'blog-list.html')
    with open(blog_list_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # We will find the entire list of posts and replace it with a loop.
    # Pattern to match everything between <!-- News Block Two -->
    
    dynamic_block = """
                    {% for post in posts %}
					<!-- News Block Two -->
					<div class="news-block-two">
						<div class="inner-box">
							<div class="image">
								<a href="{{ post.get_absolute_url }}"><img src="{{ post.image.url }}" alt="" /></a>
							</div>
							<div class="lower-content">
								<ul class="post-info">
									<li><a href="{{ post.get_absolute_url }}"><span class="icon fa fa-eye"></span>109 Views</a></li>
									<li><a href="{{ post.get_absolute_url }}"><span class="icon fa fa-comment"></span>12</a></li>
									<li><a href="{{ post.get_absolute_url }}"><span class="icon fa fa-bookmark-o"></span>{{ post.category.name }}</a></li>
								</ul>
								<h2><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h2>
								<div class="text">{{ post.content|truncatewords:20 }}</div>
								<a href="{{ post.get_absolute_url }}" class="learn-more">Learn More <span class="icon flaticon-right-arrow-1"></span></a>
							</div>
						</div>
					</div>
					{% endfor %}
"""
    
    # Let's just use string replace on a large block, or regex.
    # The news blocks start after <div class="row clearfix"> which is around line 155, inside <div class="col-lg-8 col-md-12 col-sm-12">
    import re
    # We can replace everything from the first <!-- News Block Two --> up to <!-- Styled Pagination -->
    html = re.sub(r'<!-- News Block Two -->.*?<!-- Styled Pagination -->', dynamic_block + '\n<!-- Styled Pagination -->', html, flags=re.DOTALL)
    
    with open(blog_list_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Done")
