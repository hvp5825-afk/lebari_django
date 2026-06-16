import os
import glob

tpl_dir = r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates'
for path in glob.glob(os.path.join(tpl_dir, '*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<li><a href="{% url \'index\' %}">Coaching</a></li>' in content:
        content = content.replace('<li><a href="{% url \'index\' %}">Coaching</a></li>', '<li><a href="{% url \'coaching\' %}">Coaching</a></li>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {os.path.basename(path)}')
