import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lebari_project.settings')
django.setup()

from blog.models import Post

# Paths to static images
static_images = [
    'static/images/resource/news-1.jpg',
    'static/images/resource/news-2.jpg',
    'static/images/resource/news-3.jpg',
    'static/images/resource/news-4.jpg',
    'static/images/resource/news-5.jpg',
    'static/images/resource/news-15.jpg',
    'static/images/resource/news-16.jpg',
    'static/images/resource/news-17.jpg',
]

posts = Post.objects.all()

if not posts.exists():
    print("No blog posts found. Please create some blog posts first.")
else:
    for i, post in enumerate(posts):
        image_path = static_images[i % len(static_images)]
        full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), image_path)
        
        if os.path.exists(full_path):
            with open(full_path, 'rb') as f:
                post.image.save(os.path.basename(image_path), File(f), save=True)
            print(f"Updated post '{post.title}' with image '{os.path.basename(image_path)}'")
        else:
            print(f"Image not found: {full_path}")

print("Blog photos population complete!")
