import os
from PIL import Image

def create_blank_logo(dest_path):
    # Create 1x1 completely transparent image
    img = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
    img.save(dest_path, "PNG")
    print(f"Created blank transparent logo at {dest_path}")

if __name__ == "__main__":
    img_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static\images"
    img2_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static\images2"
    
    tasks = [
        os.path.join(img_dir, "logo.png"),
        os.path.join(img_dir, "logo-2.png"),
        os.path.join(img2_dir, "logo-2.png"),
    ]
    
    for dest in tasks:
        create_blank_logo(dest)
