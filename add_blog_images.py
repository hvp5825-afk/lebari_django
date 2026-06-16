import os
import django
from PIL import Image

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lebari_project.settings')
django.setup()

from blog.models import Post

def resize_and_crop(img_path, dest_path, target_size=(435, 468)):
    with Image.open(img_path) as img:
        img = img.convert("RGBA")
        img_aspect = img.width / img.height
        target_aspect = target_size[0] / target_size[1]
        
        if img_aspect > target_aspect:
            # Crop width
            new_width = int(target_aspect * img.height)
            offset = (img.width - new_width) / 2
            crop_box = (offset, 0, img.width - offset, img.height)
        else:
            # Crop height
            new_height = int(img.width / target_aspect)
            offset = (img.height - new_height) / 2
            crop_box = (0, offset, img.width, img.height - offset)
            
        img = img.crop(crop_box)
        img = img.resize(target_size, Image.Resampling.LANCZOS)
        img.save(dest_path, "PNG")
        print(f"Saved {dest_path} with size {target_size}")

def update_blog_images():
    media_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\media\blogs"
    os.makedirs(media_dir, exist_ok=True)
    
    # Paths to generated images
    img1_src = r"C:\Users\Harsh\.gemini\antigravity-ide\brain\69564934-de77-4300-8f5b-b1adc2491abf\news_article_1_1781519966738.png"
    img2_src = r"C:\Users\Harsh\.gemini\antigravity-ide\brain\69564934-de77-4300-8f5b-b1adc2491abf\news_article_2_1781519980925.png"
    
    img1_dest = os.path.join(media_dir, "blog_ai.png")
    img2_dest = os.path.join(media_dir, "blog_study.png")
    
    # Resize and save
    resize_and_crop(img1_src, img1_dest)
    resize_and_crop(img2_src, img2_dest)
    
    # Update DB
    post1 = Post.objects.filter(title__icontains="Future of AI").first()
    if post1:
        post1.image.name = "blogs/blog_ai.png"
        post1.save()
        print("Updated Future of AI in Education image")
        
    post2 = Post.objects.filter(title__icontains="Top 5 Study Habits").first()
    if post2:
        post2.image.name = "blogs/blog_study.png"
        post2.save()
        print("Updated Top 5 Study Habits image")

if __name__ == "__main__":
    update_blog_images()
