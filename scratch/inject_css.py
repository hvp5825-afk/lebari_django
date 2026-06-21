import os

target_files = [
    'blog-list.html',
    'course-2.html',
    'course-3.html',
    'course-4.html',
    'donation.html',
    'index-2.html',
    'index-3.html',
    'index-4.html',
    'index-5.html',
    'membership.html',
    'not-found.html',
    'profile.html'
]

for filename in target_files:
    path = os.path.join('templates', filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        if 'custom-animations.css' in content:
            print(f'Already has custom-animations.css: {filename}')
            continue
            
        # Look for responsive.css to insert after it
        lines = content.split('\n')
        updated = False
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if 'responsive.css' in line and not updated:
                new_lines.append("<link href=\"{% static 'css/custom-animations.css' %}?v=1.0\" rel=\"stylesheet\">")
                updated = True
                
        if updated:
            with open(path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))
            print(f'Successfully updated: {filename}')
        else:
            print(f'Could not find responsive.css in: {filename}')
