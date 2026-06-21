import os
import re

templates_dir = 'templates'
for filename in os.listdir(templates_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(templates_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the search form
        new_content = re.sub(
            r'<form method="post" action="{% url \'contact\' %}">\s*{% csrf_token %}\s*<div class="form-group">\s*<input type="search" name="search-field"',
            r'<form method="GET" action="{% url \'course_list\' %}">\n\t\t\t\t\t\t\t\t<div class="form-group">\n\t\t\t\t\t\t\t\t\t<input type="search" name="q"',
            content
        )
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {filename}')
