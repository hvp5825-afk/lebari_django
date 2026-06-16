import re
import os

with open(r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates\course-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

images = set()
for match in re.findall(r"{% static '([^']+)' %}", text):
    if match.endswith('.jpg') or match.endswith('.png'):
        images.add(match)

static_dir = r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static'
missing = []
for img in sorted(images):
    p = os.path.join(static_dir, img.replace('/', '\\'))
    if os.path.exists(p):
        print(f'EXISTS: {img}')
    else:
        print(f'MISSING: {img}')
        missing.append(img)
