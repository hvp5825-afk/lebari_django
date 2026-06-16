import os
import django
from PIL import Image

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lebari_project.settings')
django.setup()

from courses.models import Course

def resize_and_crop(img_path, dest_path, target_size=(370, 436)):
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

def update_digital_marketing_course():
    media_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\media\courses"
    os.makedirs(media_dir, exist_ok=True)
    
    # Pick an existing generated image for marketing
    img_src = r"C:\Users\Harsh\.gemini\antigravity-ide\brain\69564934-de77-4300-8f5b-b1adc2491abf\feature_main_1781519382215.png"
    img_dest = os.path.join(media_dir, "digital_marketing.png")
    
    resize_and_crop(img_src, img_dest)
    
    course = Course.objects.filter(title__icontains="Digital Marketing").first()
    if course:
        course.image.name = "courses/digital_marketing.png"
        course.save()
        print("Updated Digital Marketing Course image")

if __name__ == "__main__":
    update_digital_marketing_course()
