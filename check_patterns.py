import re

with open(r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates\course-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Pattern tags:')
for m in re.findall(r'<div class="pattern-layer[^"]*"[^>]*>', text):
    print(m)
