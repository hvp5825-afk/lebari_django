import re

with open(r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates\course.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<a href="([^"]+)">', text)
for m in matches[:10]:
    print(m)
