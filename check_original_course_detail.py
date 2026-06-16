import re

with open(r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari-package\lebari\course-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

images = set(re.findall(r'src="([^"]+)"', text))
images.update(re.findall(r'url\(([^)]+)\)', text))

print('Images in original course-detail.html:')
for img in sorted(images):
    if img.endswith('.jpg') or img.endswith('.png'):
        print(img)
