import os
from PIL import Image

def pad_and_resize_logo(img_path, dest_path, target_size=(150, 70), pad_color=(255, 255, 255)):
    with Image.open(img_path) as img:
        img = img.convert("RGBA")
        
        # Calculate aspect ratios
        img_aspect = img.width / img.height
        target_aspect = target_size[0] / target_size[1]
        
        if img_aspect > target_aspect:
            # Image is wider than target. Scale based on width.
            new_width = target_size[0]
            new_height = int(new_width / img_aspect)
        else:
            # Image is taller than target. Scale based on height.
            new_height = target_size[1]
            new_width = int(new_height * img_aspect)
            
        # Resize image
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Create new image with target size and pad color
        new_img = Image.new("RGBA", target_size, pad_color + (255,))
        
        # Calculate paste position
        x_offset = (target_size[0] - new_width) // 2
        y_offset = (target_size[1] - new_height) // 2
        
        # Paste using alpha channel as mask
        new_img.paste(resized_img, (x_offset, y_offset), resized_img)
        
        new_img.save(dest_path, "PNG")
        print(f"Saved {dest_path} with size {target_size}")

if __name__ == "__main__":
    base_dir = r"C:\Users\Harsh\.gemini\antigravity-ide\brain\69564934-de77-4300-8f5b-b1adc2491abf"
    logo_src = os.path.join(base_dir, "lebari_premium_logo_1781600640683.png")
    
    img_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static\images"
    img2_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static\images2"
    
    tasks = [
        (logo_src, os.path.join(img_dir, "logo.png"), (150, 70)),
        (logo_src, os.path.join(img_dir, "logo-2.png"), (150, 70)),
        (logo_src, os.path.join(img2_dir, "logo-2.png"), (160, 60)),
    ]
    
    for src, dest, size in tasks:
        if os.path.exists(src):
            pad_and_resize_logo(src, dest, size)
        else:
            print(f"Source not found: {src}")
