import os
import re

original_nav = """<ul class="navigation clearfix">
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

original_footer = """<div class="row clearfix">
							<div class="column col-lg-4 col-md-4 col-sm-12">
								<h5>About</h5>
								<ul class="list">
									<li><a href="{% url 'about' %}">About Us</a></li>
									<li><a href="{% url 'blog_list' %}">News & Blog</a></li>
									<li><a href="{% url 'teacher' %}">Our Team</a></li>
									<li><a href="{% url 'contact' %}">Contact Us</a></li>
								</ul>
							</div>
							<!-- Column -->
							<div class="column col-lg-4 col-md-4 col-sm-12">
								<h5>Need some help?</h5>
								<ul class="list">
									<li><a href="{% url 'faq' %}">FAQs</a></li>
									<li><a href="{% url 'contact' %}">Help Centre</a></li>
									<li><a href="{% url 'register' %}">Create Account</a></li>
									<li><a href="{% url 'login' %}">Login</a></li>
								</ul>
							</div>
							<!-- Column -->
							<div class="column col-lg-4 col-md-4 col-sm-12">
								<h5>Links</h5>
								<ul class="list">
									<li><a href="{% url 'course_list' %}">All Courses</a></li>
									<li><a href="{% url 'membership' %}">Membership</a></li>
									<li><a href="{% url 'event_list' %}">Events</a></li>
									<li><a href="{% url 'donation' %}">Donation</a></li>
								</ul>
							</div>
						</div>"""

def revert_nav(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'<ul class="navigation clearfix">.*?</ul>', original_nav, content, flags=re.DOTALL)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
def revert_footer(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<!-- Footer Column -->' in content:
        parts = content.split('<!-- Footer Column -->')
        if len(parts) > 2:
            sub_parts = parts[2].split('<!-- Lower Box -->')
            if len(sub_parts) > 1:
                footer_links_section = sub_parts[0]
                new_links_section = re.sub(
                    r'<div class="row clearfix">.*?</div>\s*</div>\s*</div>\s*</div>',
                    original_footer + '\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>',
                    footer_links_section,
                    flags=re.DOTALL
                )
                parts[2] = new_links_section + '<!-- Lower Box -->' + sub_parts[1]
                content = '<!-- Footer Column -->'.join(parts)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

revert_nav('templates/base.html')
revert_nav('templates/index-2.html')
revert_footer('templates/base.html')
revert_footer('templates/index-2.html')

print("Reverted HTML templates!")
