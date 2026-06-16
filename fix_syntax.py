import os
import glob

template_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates"

for filepath in glob.glob(os.path.join(template_dir, "*.html")):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace literal \ followed by ' with just '
    if "\\'" in content:
        new_content = content.replace("\\'", "'")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {os.path.basename(filepath)}")
