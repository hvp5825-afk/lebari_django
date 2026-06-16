import re
file_path = r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates\course-detail.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'<h2>\{\{\s*course\.title\|safe\s*\}\}</h2>', r'<h2>The Complete JavaScript Course 2020 <br> From Zero to Expert!</h2>', text)
text = re.sub(r'<div class="development">\{\{\s*course\.category\.name\s*\}\}</div>', r'<div class="development">Development courses</div>', text)
text = re.sub(r'<div class="hovers">\{\{\s*course\.duration\s*\}\}\s*\.\s*\{\{\s*course\.level\s*\}\}</div>', r'<div class="hovers">11.5 total hours . All Levels  </div>', text)
text = re.sub(r'<div class="price">\$\{\{\s*course\.price\s*\}\}\s*<i>\$129\.99</i>\s*<span>92%\s*of</span></div>', r'<div class="price">$9.99 <i>$129.99</i> <span>92% of</span></div>', text)
text = re.sub(r'<li>Level :<span>\{\{\s*course\.level\s*\}\}</span></li>', r'<li>Level :<span>Beginner</span></li>', text)
text = re.sub(r'<li>Topic :<span>\{\{\s*course\.category\.name\s*\}\}</span></li>', r'<li>Topic :<span>Java Script</span></li>', text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Reverted dynamic tags back to hardcoded dummy text to match screenshot.')
