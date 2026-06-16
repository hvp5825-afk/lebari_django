import os
import re

original_path = r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari-package\lebari\index.html'
django_path = r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates\index.html'

with open(original_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Extract content between <!-- Banner Section --> and the footer
# Wait, let's just find the start of the actual content and end of content.
start_idx = text.find('<!-- Banner Section -->')
# Find the footer
end_idx = text.find('<footer class="main-footer">')

if start_idx != -1 and end_idx != -1:
    body = text[start_idx:end_idx]
else:
    body = text

# Convert images to static tags
def replace_img(match):
    path = match.group(1)
    if not path.startswith('{%'):
        return f'src="{{% static \'{path}\' %}}"'
    return match.group(0)

body = re.sub(r'src="([^"]+)"', replace_img, body)

# Convert url() in styles
def replace_url(match):
    path = match.group(1).strip("'\"")
    if not path.startswith('{%'):
        return f'url({{% static \'{path}\' %}})'
    return match.group(0)

body = re.sub(r'url\(([^)]+)\)', replace_url, body)

# Add django template tags
final_html = "{% extends 'base.html' %}\n{% load static %}\n\n{% block content %}\n\n" + body + "\n{% endblock %}\n"

with open(django_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Successfully replaced index.html with original template content and added Django tags.")
