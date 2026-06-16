import os
from PIL import Image

def apply_mask_and_save(src_img_path, original_template_img_path, dest_path):
    with Image.open(original_template_img_path) as orig_img:
        orig_img = orig_img.convert("RGBA")
        target_size = orig_img.size
        # Extract the alpha channel to use as a mask
        mask = orig_img.split()[3]
        
    with Image.open(src_img_path) as src_img:
        src_img = src_img.convert("RGBA")
        
        # Crop src_img to match target aspect ratio
        img_aspect = src_img.width / src_img.height
        target_aspect = target_size[0] / target_size[1]
        
        if img_aspect > target_aspect:
            new_width = int(target_aspect * src_img.height)
            offset = (src_img.width - new_width) / 2
            crop_box = (offset, 0, src_img.width - offset, src_img.height)
        else:
            new_height = int(src_img.width / target_aspect)
            offset = (src_img.height - new_height) / 2
            crop_box = (0, offset, src_img.width, src_img.height - offset)
            
        src_img = src_img.crop(crop_box)
        src_img = src_img.resize(target_size, Image.Resampling.LANCZOS)
        
        # Apply the mask
        src_img.putalpha(mask)
        
        src_img.save(dest_path, "PNG")
        print(f"Saved {dest_path} with size {target_size} and proper mask applied.")

if __name__ == "__main__":
    base_dir = r"C:\Users\Harsh\.gemini\antigravity-ide\brain\69564934-de77-4300-8f5b-b1adc2491abf"
    slider_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static\images\main-slider"
    
    img_1_src = os.path.join(base_dir, "hero_student_learning_1781517350974.png")
    img_4_src = os.path.join(base_dir, "learning_laptop_closeup_1781517364967.png")
    
    img_1_orig = os.path.join(slider_dir, "image-1.png")
    img_4_orig = os.path.join(slider_dir, "image-4.png")
    
    img_1_dest = os.path.join(slider_dir, "image-1.png")
    img_4_dest = os.path.join(slider_dir, "image-4.png")
    
    # Apply and overwrite
    apply_mask_and_save(img_1_src, img_1_orig, img_1_dest)
    apply_mask_and_save(img_4_src, img_4_orig, img_4_dest)
