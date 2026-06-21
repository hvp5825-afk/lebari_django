import os

filepath = 'templates/course-detail.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '<h5>Courses Description</h5>': '<h5>{{ labels.course_tab_description|default:"Courses Description" }}</h5>',
    "<h5>What you'll learn</h5>": "<h5>{{ labels.course_what_learn|default:'What you\\'ll learn' }}</h5>",
    '<h5>Requirements</h5>': '<h5>{{ labels.course_requirements|default:"Requirements" }}</h5>',
    '<h5>Course content</h5>': '<h5>{{ labels.course_content|default:"Course content" }}</h5>',
    '<h5>Instructor</h5>': '<h5>{{ labels.course_instructor_title|default:"Instructor" }}</h5>',
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
