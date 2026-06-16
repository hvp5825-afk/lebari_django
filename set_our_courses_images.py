import os
from PIL import Image

def resize_and_crop(img_path, dest_path, target_size):
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
    resource_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static\images\resource"
    os.makedirs(resource_dir, exist_ok=True)
    
    # Generated artifact paths
    base_dir = r"C:\Users\Harsh\.gemini\antigravity-ide\brain\69564934-de77-4300-8f5b-b1adc2491abf"
    images = [
        os.path.join(base_dir, "feature_main_1781519382215.png"),
        os.path.join(base_dir, "learning_laptop_closeup_1781517364967.png"),
        os.path.join(base_dir, "hero_student_learning_1781517350974.png"),
        os.path.join(base_dir, "career_change_1781519768361.png"),
        os.path.join(base_dir, "news_article_1_1781519966738.png"),
        os.path.join(base_dir, "news_article_2_1781519980925.png")
    ]
    
    # Target sizes
    sizes = [(370, 436)] * 3 + [(370, 240)] * 3
    
    for i in range(6):
        dest = os.path.join(resource_dir, f"course-{i+1}.jpg")
        resize_and_crop(images[i], dest, sizes[i])
