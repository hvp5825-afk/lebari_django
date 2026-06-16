with open(r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates\course-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('href="index.html"', 'href="{% url \'index\' %}"')
with open(r'c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates\course-detail.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Fixed links')
