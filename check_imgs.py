import re

with open(r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

images = set()
for match in re.findall(r"{% static '([^']+)' %}", text):
    if match.endswith('.jpg') or match.endswith('.png'):
        images.add(match)

import os
static_dir = r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\static'
for img in sorted(images):
    p = os.path.join(static_dir, img.replace('/', '\\'))
    if os.path.exists(p):
        print(f"EXISTS: {img} ({os.path.getsize(p)} bytes)")
    else:
        print(f"MISSING: {img}")
