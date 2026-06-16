import os
from PIL import Image

def resize_and_crop(img_path, dest_path, target_size, save_format):
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
        
        if save_format == "JPEG":
            img = img.convert("RGB")
            
        img.save(dest_path, save_format, quality=95)
        print(f"Saved {dest_path} with size {target_size}")

if __name__ == "__main__":
    base_dir = r"C:\Users\Harsh\.gemini\antigravity-ide\brain\69564934-de77-4300-8f5b-b1adc2491abf"
    resource_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static\images2\resource"
    os.makedirs(resource_dir, exist_ok=True)
    
    tasks = [
        ("hero_student_learning_1781517350974.png", "about-4.jpg", (493, 522), "JPEG"),
        ("learning_laptop_closeup_1781517364967.png", "about-5.jpg", (246, 282), "JPEG"),
        ("feature_main_1781519382215.png", "study.jpg", (945, 646), "JPEG"),
        
        ("news_article_1_1781519966738.png", "course-1.jpg", (319, 293), "JPEG"),
        ("news_article_2_1781519980925.png", "course-2.jpg", (319, 293), "JPEG"),
        ("career_change_1781519768361.png", "course-3.jpg", (319, 293), "JPEG"),
        ("feature_main_dark_1781519640150.png", "course-4.jpg", (319, 293), "JPEG"),
        ("special_classroom_1781519954060.png", "course-5.jpg", (319, 293), "JPEG"),
        ("benefit_1_1781519015581.png", "course-6.jpg", (319, 293), "JPEG"),
        
        ("benefit_2_1781519028659.png", "campus-1.jpg", (383, 444), "JPEG"),
        ("benefit_3_1781519042659.png", "campus-2.jpg", (383, 444), "JPEG"),
        ("learning_laptop_closeup_1781517364967.png", "campus-3.jpg", (383, 444), "JPEG"),
        ("feature_main_1781519382215.png", "campus-4.jpg", (383, 444), "JPEG")
    ]
    
    for src_name, dest_name, size, fmt in tasks:
        src = os.path.join(base_dir, src_name)
        dest = os.path.join(resource_dir, dest_name)
        if os.path.exists(src):
            resize_and_crop(src, dest, size, fmt)
        else:
            print(f"Source not found: {src}")
