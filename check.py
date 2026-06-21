import re

def check_html(filepath, prefix):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = re.findall(r'<a[^>]*class=[\'"](?:theme-btn|read-more)[^>]*>.*?</a>', content, re.DOTALL)
    for m in matches:
        print(f"{filepath}: {m.replace(chr(10), ' ').strip()[:150]}")

check_html('templates/index-2.html', 'homepage')
check_html('templates/about.html', 'aboutpage')
check_html('templates/blog.html', 'blogpage')
