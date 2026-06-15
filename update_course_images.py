import os
import django
from PIL import Image

# Setup Django
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
        
        # Convert back to RGB for saving as JPG if needed, but PNG supports RGBA
        if dest_path.endswith('.jpg'):
            img = img.convert("RGB")
            img.save(dest_path, "JPEG")
        else:
            img.save(dest_path, "PNG")
        print(f"Saved {dest_path} with size {target_size}")

def update_courses():
    media_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\media\courses"
    os.makedirs(media_dir, exist_ok=True)
    
    # Paths to generated images
    img1_src = r"C:\Users\Harsh\.gemini\antigravity-ide\brain\69564934-de77-4300-8f5b-b1adc2491abf\learning_laptop_closeup_1781517364967.png"
    img2_src = r"C:\Users\Harsh\.gemini\antigravity-ide\brain\69564934-de77-4300-8f5b-b1adc2491abf\hero_student_learning_1781517350974.png"
    
    img1_dest = os.path.join(media_dir, "ui_ux_course.png")
    img2_dest = os.path.join(media_dir, "python_course.png")
    
    # Resize and save
    resize_and_crop(img1_src, img1_dest)
    resize_and_crop(img2_src, img2_dest)
    
    # Update DB
    course1 = Course.objects.filter(title__icontains="UI/UX Masterclass").first()
    if course1:
        course1.image.name = "courses/ui_ux_course.png"
        course1.save()
        print("Updated Advanced UI/UX Masterclass image")
        
    course2 = Course.objects.filter(title__icontains="Python Bootcamp").first()
    if course2:
        course2.image.name = "courses/python_course.png"
        course2.save()
        print("Updated Complete Python Bootcamp image")

if __name__ == "__main__":
    update_courses()
