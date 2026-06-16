import os
from PIL import Image

def resize_and_crop(img_path, dest_path, target_size=(507, 517)):
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
        
        # Save as PNG
        img.save(dest_path, "PNG")
        print(f"Saved {dest_path} with size {target_size}")

if __name__ == "__main__":
    resource_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static\images\resource"
    os.makedirs(resource_dir, exist_ok=True)
    
    img_src = r"C:\Users\Harsh\.gemini\antigravity-ide\brain\69564934-de77-4300-8f5b-b1adc2491abf\special_classroom_1781519954060.png"
    img_dest = os.path.join(resource_dir, "event.png")
    
    resize_and_crop(img_src, img_dest)
