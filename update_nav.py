import os

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Define old and new nav
    import re
    old_nav_pattern = r'<ul class="navigation clearfix">.*?</ul>'
    
    new_nav = '''<ul class="navigation clearfix">
								{% for item in main_menu %}
									{% if item.children.all %}
										<li class="dropdown {% if request.path == item.url %}current{% endif %}"><a href="{{ item.url }}">{{ item.title }}</a>
											<ul>
												{% for child in item.children.all %}
													<li class="{% if request.path == child.url %}current{% endif %}"><a href="{{ child.url }}">{{ child.title }}</a></li>
												{% endfor %}
											</ul>
										</li>
									{% else %}
										<li class="{% if request.path == item.url %}current{% endif %}"><a href="{{ item.url }}">{{ item.title }}</a></li>
									{% endif %}
								{% endfor %}
								
								{% if user.is_authenticated %}
								<li class="dropdown {% if 'profile' in request.resolver_match.url_name %}current{% endif %}"><a href="#">Profile</a>
									<ul>
										<li><a href="{% url 'profile' %}">Dashboard</a></li>
										<li><a href="{% url 'logout' %}">Logout</a></li>
									</ul>
								</li>
								{% else %}
								<li><a href="{% url 'login' %}">Login / Register</a></li>
								{% endif %}
							</ul>'''
    
    # We might match multiple occurrences if there's mobile menu
    content = re.sub(old_nav_pattern, new_nav, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('templates/base.html')
update_file('templates/index-2.html')

print("Updated navigation menus!")
