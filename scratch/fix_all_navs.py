import os
import re

TARGET_DIR = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates"

NEW_NAV = """							<ul class="navigation clearfix">
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
							</ul>"""

def update_files():
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Match the entire <ul class="navigation clearfix">...</ul>
                pattern = re.compile(r'<ul class="navigation clearfix">.*?</ul>', re.DOTALL)
                
                if pattern.search(content):
                    # Replace
                    new_content = pattern.sub(NEW_NAV, content)
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated navigation in {file}")

if __name__ == "__main__":
    update_files()
