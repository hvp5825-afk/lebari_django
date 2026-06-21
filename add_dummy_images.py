import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lebari_django.settings')
django.setup()

from blog.models import Post
from core.models import BlogPageSetting

# Set default post image in BlogPageSetting
bps = BlogPageSetting.objects.first()
if bps:
    source_path = 'static/images/resource/news-15.jpg'
    if os.path.exists(source_path):
        with open(source_path, 'rb') as f:
            bps.default_post_image.save('news-15.jpg', File(f), save=True)

# Set images for existing posts
posts = Post.objects.all()[:5]
dummy_images = ['news-16.jpg', 'news-17.jpg', 'news-18.jpg', 'news-19.jpg', 'news-20.jpg']

for i, post in enumerate(posts):
    if i < len(dummy_images):
        img_name = dummy_images[i]
        src = f'static/images/resource/{img_name}'
        if os.path.exists(src):
            with open(src, 'rb') as f:
                post.image.save(img_name, File(f), save=True)

print('Successfully added dummy images to BlogPageSetting and existing Posts.')
