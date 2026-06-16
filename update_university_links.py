import os
import glob

tpl_dir = r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates'
for path in glob.glob(os.path.join(tpl_dir, '*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We might have '<a href="{% url \'index\' %}">University <span class="new-page">New</span></a>'
    # Or just 'University'
    # Let's replace only the href part for the University link.
    if '>University <span class="new-page">New</span></a>' in content:
        content = content.replace('<a href="{% url \'index\' %}">University <span class="new-page">New</span></a>', '<a href="{% url \'university\' %}">University <span class="new-page">New</span></a>')
        
    # Also check if there's any simple University link
    if '<li><a href="{% url \'index\' %}">University</a></li>' in content:
        content = content.replace('<li><a href="{% url \'index\' %}">University</a></li>', '<li><a href="{% url \'university\' %}">University</a></li>')
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {os.path.basename(path)}')
