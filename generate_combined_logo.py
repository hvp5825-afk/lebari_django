import os
from PIL import Image, ImageDraw, ImageFont

def create_combined_logo(icon_path, dest_path, target_size=(150, 70), text="Lebari", text_color=(20, 30, 80)):
    # Create white background image
    img = Image.new("RGBA", target_size, (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Process icon
    try:
        with Image.open(icon_path) as icon:
            icon = icon.convert("RGBA")
            # Crop the center 512x512 from 1024x1024 to remove white space
            width, height = icon.size
            crop_box = (width//4, height//4, width*3//4, height*3//4)
            icon = icon.crop(crop_box)
            
            # Resize icon to 40x40
            icon_size = 40
            icon = icon.resize((icon_size, icon_size), Image.Resampling.LANCZOS)
            
            # Paste icon on the left
            icon_x = 5
            icon_y = (target_size[1] - icon_size) // 2
            # Create a mask from icon alpha channel if any, else None
            # The AI image has white bg, so we just paste it
            img.paste(icon, (icon_x, icon_y), icon)
    except Exception as e:
        print(f"Error processing icon: {e}")
        icon_x = 0
        icon_size = 0
        
    # Process text
    font_path = r"C:\Windows\Fonts\segoeuib.ttf" # Segoe UI Bold
    if not os.path.exists(font_path):
        font_path = r"C:\Windows\Fonts\arialbd.ttf"
    
    try:
        # Use a nice large font size for the remaining space
        font_size = 32
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    
    # Text position
    text_x = icon_x + icon_size + 5
    bbox = draw.textbbox((0, 0), text, font=font)
    text_h = bbox[3] - bbox[1]
    text_y = (target_size[1] - text_h) // 2 - 4 # slightly adjust up for visual center
    
    # Draw text
    draw.text((text_x, text_y), text, font=font, fill=text_color)
    
    img.save(dest_path, "PNG")
    print(f"Created professional combined logo at {dest_path}")

if __name__ == "__main__":
    base_dir = r"C:\Users\Harsh\.gemini\antigravity-ide\brain\69564934-de77-4300-8f5b-b1adc2491abf"
    icon_src = os.path.join(base_dir, "premium_education_icon_1781601095227.png")
    
    img_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static\images"
    img2_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static\images2"
    
    tasks = [
        (os.path.join(img_dir, "logo.png"), (150, 70)),
        (os.path.join(img_dir, "logo-2.png"), (150, 70)),
        (os.path.join(img2_dir, "logo-2.png"), (160, 60)),
    ]
    
    for dest, size in tasks:
        create_combined_logo(icon_src, dest, size)
