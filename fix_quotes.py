import os
import glob
import re

template_dir = 'templates'
html_files = glob.glob(os.path.join(template_dir, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    # Replace escaped single quotes back to normal single quotes inside default tag
    # Specifically looking for: |default:\'Your email\'
    content = content.replace(r"\'Your email\'", "'Your email'")
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {os.path.basename(filepath)}")

print("Fix complete.")
