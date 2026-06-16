import os
import re
import shutil

original_path = r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari-package\lebari\course-detail.html'
django_path = r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates\course-detail.html'

with open(original_path, 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('<!-- Cource Detail Banner Section -->')
end_idx = text.find('<footer class="main-footer">')

if start_idx != -1 and end_idx != -1:
    body = text[start_idx:end_idx]
else:
    body = text

def replace_img(match):
    path = match.group(1)
    if not path.startswith('{%'):
        return f'src="{{% static \'{path}\' %}}"'
    return match.group(0)

body = re.sub(r'src="([^"]+)"', replace_img, body)

def replace_url(match):
    path = match.group(1).strip("'\"")
    if not path.startswith('{%'):
        return f'url({{% static \'{path}\' %}})'
    return match.group(0)

body = re.sub(r'url\(([^)]+)\)', replace_url, body)

# Now wait, Django's view passes `{{ course.title|safe }}`, `{{ course.description|safe }}` etc.
# We must preserve the Django variables for the course details!
# Let's read the OLD django_path to see what variables we need to re-inject.
with open(django_path, 'r', encoding='utf-8') as f:
    old_django = f.read()

# We can see {{ course.title|safe }} is inside <h2> tags.
body = re.sub(r'<h2>Introduction to Web Programming</h2>', '<h2>{{ course.title|safe|default:"Introduction to Web Programming" }}</h2>', body)

body = re.sub(r'<li><span class="icon fa fa-clock-o"></span>Last Update : November 23, 2020</li>', '<li><span class="icon fa fa-clock-o"></span>Last Update : {{ course.updated_at|date:"M d, Y"|default:"November 23, 2020" }}</li>', body)

# Replace Courses Description
# The original has a paragraph for description.
# In old django, it was {{ course.description|safe }} after <h5>Courses Description</h5>
body = re.sub(r'(<h5>Courses Description</h5>\s*<p>).*?(</p>)', r'\1{{ course.description|safe|default:"We offer a broad range of..." }}\2', body, flags=re.DOTALL)

# Price
body = re.sub(r'<div class="price">\$46</div>', '<div class="price">${{ course.price|default:"46" }}</div>', body)
# Category
body = re.sub(r'<li>Topic :<span>Business</span></li>', '<li>Topic :<span>{{ course.category.name|default:"Business" }}</span></li>', body)
# Level
body = re.sub(r'<li>Level :<span>Basic</span></li>', '<li>Level :<span>{{ course.level|default:"Basic" }}</span></li>', body)
# Duration
body = re.sub(r'<div class="hovers">15 Hours . Beginner</div>', '<div class="hovers">{{ course.duration|default:"15 Hours" }} . {{ course.level|default:"Beginner" }}</div>', body)


final_html = "{% extends 'base.html' %}\n{% load static %}\n\n{% block content %}\n\n" + body + "\n{% endblock %}\n"

with open(django_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Successfully replaced course-detail.html with original template content and added Django tags.")
