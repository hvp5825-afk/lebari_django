import os
import glob

template_dir = 'templates'
html_files = glob.glob(os.path.join(template_dir, '*.html'))

hardcoded_patterns_to_check = [
    'Newsletter',
    'Your email',
    'Get started now',
    'Subscribe',
    'Categories',
    'Recent Posts',
    'Tags',
    'Leave a Reply',
    'Submit',
    'Description',
    'Reviews',
    'Curriculum',
    'Instructor',
    'Filter',
    'Price',
    'Level',
    'Language',
    'Duration',
    'Share',
]

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    found = []
    for pattern in hardcoded_patterns_to_check:
        if pattern in content:
            # Simple check if the string is just plain text, not in a context variable
            if '{%' not in pattern and '{{' not in pattern:
                found.append(pattern)
            
    if found:
        print(f'--- {os.path.basename(filepath)} ---')
        print(f'Found: {", ".join(found)}')
