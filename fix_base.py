import re

original_nav = '''<ul class="navigation clearfix">
								<li class="{% if request.resolver_match.url_name == 'index' %}current{% endif %}"><a href="{% url 'index' %}">Home</a></li>
								<li class="dropdown {% if 'about' in request.resolver_match.url_name or 'teacher' in request.resolver_match.url_name %}current{% endif %}"><a href="#">About</a>
									<ul>
										<li><a href="{% url 'about' %}">About Us</a></li>
										<li><a href="{% url 'faq' %}">Faq</a></li>
										<li><a href="{% url 'teacher' %}">Teachers</a></li>
										<li><a href="{% url 'membership' %}">Membership</a></li>
										<li><a href="{% url 'event_list' %}">Events</a></li>
									</ul>
								</li>
								<li class="{% if 'course' in request.resolver_match.url_name %}current{% endif %}"><a href="{% url 'course_list' %}">Courses</a></li>
								<li class="{% if 'blog' in request.resolver_match.url_name %}current{% endif %}"><a href="{% url 'blog_list' %}">Blog</a></li>
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
								<li class="{% if request.resolver_match.url_name == 'contact' %}current{% endif %}"><a href="{% url 'contact' %}">Contact</a></li>
							</ul>'''

with open('templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<ul class="navigation clearfix">.*?<!-- Main Menu End-->'

new_part = original_nav + '''
							</div>
						</nav>
						<!-- Main Menu End-->'''

content = re.sub(pattern, new_part, content, flags=re.DOTALL)

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(content)
