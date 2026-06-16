import os
from PIL import Image

def resize_and_crop(img_path, dest_path, target_size=(370, 365)):
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
        print(f"Saved {dest_path} with size {target_size}")

if __name__ == "__main__":
    base_dir = r"C:\Users\Harsh\.gemini\antigravity-ide\brain\69564934-de77-4300-8f5b-b1adc2491abf"
    resource_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static\images2\resource"
    os.makedirs(resource_dir, exist_ok=True)
    
    tasks = [
        ("special_classroom_1781519954060.png", "event-10.jpg", (751, 396)),
        ("hero_student_learning_1781517350974.png", "event-4.jpg", (370, 365)),
        ("feature_main_1781519382215.png", "event-5.jpg", (370, 365)),
        ("career_change_1781519768361.png", "event-6.jpg", (370, 365))
    ]
    
    for src_name, dest_name, size in tasks:
        src = os.path.join(base_dir, src_name)
        dest = os.path.join(resource_dir, dest_name)
        if os.path.exists(src):
            resize_and_crop(src, dest, size)
        else:
            print(f"Source not found: {src}")
