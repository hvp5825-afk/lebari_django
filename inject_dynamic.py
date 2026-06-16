import re

file_path = r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates\course-detail.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace dummy title with dynamic title
text = re.sub(r'<h2>The Complete JavaScript Course 2020 <br> From Zero to Expert!</h2>', r'<h2>{{ course.title|safe }}</h2>', text)

# Replace dummy category
text = re.sub(r'<div class="development">Development courses</div>', r'<div class="development">{{ course.category.name }}</div>', text)

# Replace dummy duration
text = re.sub(r'<div class="hovers">11\.5 total hours \. All Levels  </div>', r'<div class="hovers">{{ course.duration }} . {{ course.level }}</div>', text)

# Replace price
text = re.sub(r'<div class="price">\$9\.99 <i>\$129\.99</i> <span>92% of</span></div>', r'<div class="price">${{ course.price }} <i>$129.99</i> <span>92% of</span></div>', text)

# Replace topic and level in info column
text = re.sub(r'<li>Level :<span>Beginner</span></li>', r'<li>Level :<span>{{ course.level }}</span></li>', text)
text = re.sub(r'<li>Topic :<span>Java Script</span></li>', r'<li>Topic :<span>{{ course.category.name }}</span></li>', text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Injected dynamic tags successfully.")
