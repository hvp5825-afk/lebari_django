import os
import django
from django.core.files import File
from PIL import Image

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lebari_project.settings')
django.setup()

from blog.models import Post

def resize_and_crop(img_path, dest_path, target_size=(839, 558)):
    with Image.open(img_path) as img:
        img = img.convert("RGBA")
        img_aspect = img.width / img.height
        target_aspect = target_size[0] / target_size[1]
        
        if img_aspect > target_aspect:
            new_width = int(target_aspect * img.height)
            offset = (img.width - new_width) / 2
            crop_box = (offset, 0, img.width - offset, img.height)
        else:
            new_height = int(img.width / target_aspect)
            offset = (img.height - new_height) / 2
            crop_box = (0, offset, img.width, img.height - offset)
            
        img = img.crop(crop_box)
        img = img.resize(target_size, Image.Resampling.LANCZOS)
        img = img.convert("RGB")
        img.save(dest_path, "JPEG", quality=95)

if __name__ == '__main__':
    base_dir = r"C:\Users\Harsh\.gemini\antigravity-ide\brain\69564934-de77-4300-8f5b-b1adc2491abf"
    media_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\media\blogs"
    os.makedirs(media_dir, exist_ok=True)
    
    tasks = {
        "The Future of AI in Education": ("learning_laptop_closeup_1781517364967.png", "blog_ai.jpg"),
        "Top 5 Study Habits for Online Learners": ("hero_student_learning_1781517350974.png", "blog_study.jpg")
    }
    
    for title, (src_name, dest_name) in tasks.items():
        src_path = os.path.join(base_dir, src_name)
        dest_path = os.path.join(media_dir, dest_name)
        
        if os.path.exists(src_path):
            resize_and_crop(src_path, dest_path)
            
            post = Post.objects.filter(title=title).first()
            if post:
                with open(dest_path, 'rb') as f:
                    post.image.save(dest_name, File(f), save=True)
                print(f"Updated image for {title}")
        else:
            print(f"Source not found: {src_path}")
