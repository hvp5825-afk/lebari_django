import os
from PIL import Image, ImageDraw, ImageFont

def create_text_logo(dest_path, target_size=(150, 70), text="Lebari", text_color=(20, 30, 80), accent_color=(230, 180, 50)):
    # Create transparent image
    img = Image.new("RGBA", target_size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Try to load a nice font, fallback to default
    font_path = r"C:\Windows\Fonts\segoeuib.ttf" # Segoe UI Bold
    if not os.path.exists(font_path):
        font_path = r"C:\Windows\Fonts\arialbd.ttf"
    
    try:
        # Start with a large font size and shrink if needed
        font_size = 45
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
    
    # Calculate text size using textbbox
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    # Center text
    x = (target_size[0] - text_w) / 2
    y = (target_size[1] - text_h) / 2 - 5 # Shift up slightly for accent line
    
    # Draw text
    draw.text((x, y), text, font=font, fill=text_color)
    
    # Draw a gold accent line under the text
    line_y = y + text_h + 8
    draw.line([(x + 5, line_y), (x + text_w - 5, line_y)], fill=accent_color, width=3)
    
    # Add a small dot or icon accent if desired
    # draw.ellipse([(x - 12, y + 10), (x - 4, y + 18)], fill=accent_color)
    
    img.save(dest_path, "PNG")
    print(f"Created purely transparent text logo at {dest_path}")

if __name__ == "__main__":
    img_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static\images"
    img2_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static\images2"
    
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(img2_dir, exist_ok=True)
    
    tasks = [
        (os.path.join(img_dir, "logo.png"), (150, 70)),
        (os.path.join(img_dir, "logo-2.png"), (150, 70)),
        (os.path.join(img2_dir, "logo-2.png"), (160, 60)),
    ]
    
    for dest, size in tasks:
        create_text_logo(dest, size)
