content = open('templates/base.html', encoding='utf-8').read()
content = content.replace('<li class="dropdown"><a href="#">Events</a>', '<li class="dropdown"><a href="{% url \'event_list\' %}">Events</a>')
open('templates/base.html', 'w', encoding='utf-8').write(content)
print('Fixed events links in base.html')
