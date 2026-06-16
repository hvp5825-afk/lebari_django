import os
import glob
import re

def bust_cache(directory):
    for filepath in glob.glob(os.path.join(directory, '*.html')):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace {% static 'images/logo.png' %} with {% static 'images/logo.png' %}?v=1
        new_content = re.sub(r"({% static 'images/logo\.png' %})(?!\?)", r"\1?v=1", content)
        new_content = re.sub(r"({% static 'images/logo-2\.png' %})(?!\?)", r"\1?v=1", new_content)
        new_content = re.sub(r"({% static 'images2/logo-2\.png' %})(?!\?)", r"\1?v=1", new_content)
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Busted cache in {os.path.basename(filepath)}")

if __name__ == '__main__':
    base_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates"
    bust_cache(base_dir)
