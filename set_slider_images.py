import os
from PIL import Image

def resize_and_crop(img_path, dest_path, target_size=(1920, 1143)):
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
    slider_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static\images2\main-slider"
    os.makedirs(slider_dir, exist_ok=True)
    
    img_src_1 = os.path.join(base_dir, "hero_student_learning_1781517350974.png")
    img_dest_1 = os.path.join(slider_dir, "image-4.jpg")
    
    img_src_2 = os.path.join(base_dir, "special_classroom_1781519954060.png")
    img_dest_2 = os.path.join(slider_dir, "image-5.jpg")
    
    resize_and_crop(img_src_1, img_dest_1)
    resize_and_crop(img_src_2, img_dest_2)
