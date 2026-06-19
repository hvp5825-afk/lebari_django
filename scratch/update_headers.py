import os

template_dir = r"c:\Users\Harsh\Downloads\lebari-education-html-template-2025-01-26-15-55-45-utc\lebari_django\templates"

blocks = {
    'Testimonial Section': """<!-- Sec Title -->
				<div class="sec-title centered">
					<div class="title">{% if sections.PAGE_testimonials %}{{ sections.PAGE_testimonials.subtitle }}{% else %}Testimonial{% endif %}</div>
					<h2>{% if sections.PAGE_testimonials %}{{ sections.PAGE_testimonials.title|safe }}{% else %}Words From Customers{% endif %}</h2>
					<div class="text">{% if sections.PAGE_testimonials %}{{ sections.PAGE_testimonials.text|safe }}{% else %}Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu <br> fugiat nulla pariatur Duis aute irure dolor in reprehenderit in{% endif %}</div>
				</div>""",
    'News Section': """<!-- Sec Title -->
			<div class="sec-title centered">
				<div class="title">{% if sections.PAGE_news %}{{ sections.PAGE_news.subtitle }}{% else %}Our Blogs{% endif %}</div>
				<h2>{% if sections.PAGE_news %}{{ sections.PAGE_news.title|safe }}{% else %}Latest articles & news{% endif %}</h2>
				<div class="text">{% if sections.PAGE_news %}{{ sections.PAGE_news.text|safe }}{% else %}Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu <br> fugiat nulla pariatur Duis aute irure dolor in reprehenderit in{% endif %}</div>
			</div>""",
    'Banner Section': """<!-- Page Title -->
    <section class="page-title" style="background-image:url({% if sections.PAGE_banner and sections.PAGE_banner.image %}{{ sections.PAGE_banner.image.url }}{% else %}{% static 'images/background/3.jpg' %}{% endif %})">
        <div class="auto-container">
			<!-- <h1>{% if sections.PAGE_banner %}{{ sections.PAGE_banner.title|safe }}{% else %}PAGE_NAME{% endif %}</h1> -->
			<ul class="page-breadcrumb">
				<li><a href="{% url 'index' %}">home</a></li>
				<li>{% if sections.PAGE_banner %}{{ sections.PAGE_banner.title|safe }}{% else %}PAGE_NAME{% endif %}</li>
			</ul>
        </div>
    </section>
    <!-- End Page Title -->"""
}

def update_templates():
    for filename in os.listdir(template_dir):
        if not filename.endswith('.html'): continue
        filepath = os.path.join(template_dir, filename)
        
        page_prefix = filename.replace('.html', '').replace('-', '_')
        if page_prefix == 'index': page_prefix = 'home'
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # We need to find the <div class="sec-title centered">...</div> blocks for Testimonial and News
        # This is a bit tricky with regex, let's just do a simple string replace for the exact text block
        
        # Testimonial:
        old_testi = '''<div class="sec-title centered">
					<div class="title">Testimonial</div>
					<h2>Words From Customers</h2>
					<div class="text">Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu <br> fugiat nulla pariatur Duis aute irure dolor in reprehenderit in</div>
				</div>'''
        
        new_testi = blocks['Testimonial Section'].replace('PAGE_', f'{page_prefix}_')
        content = content.replace(old_testi, new_testi)
        
        # News:
        old_news = '''<div class="sec-title centered">
				<div class="title">Our Blogs</div>
				<h2>Latest articles & news</h2>
				<div class="text">Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu <br> fugiat nulla pariatur Duis aute irure dolor in reprehenderit in</div>
			</div>'''
        new_news = blocks['News Section'].replace('PAGE_', f'{page_prefix}_')
        content = content.replace(old_news, new_news)
        
        # For the generic "Duis aute irure" instances that are NOT wrapped in if sections.
        # Let's replace generic placeholder strings with dynamic text
        
        # 1. "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Duis aute irure dolor in reprehenderit in "
        content = content.replace("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Duis aute irure dolor in reprehenderit in ", "{% if sections." + page_prefix + "_content %}{{ sections." + page_prefix + "_content.text|safe }}{% else %}Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Duis aute irure dolor in reprehenderit in {% endif %}")
        
        content = content.replace("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat \n nulla pariatur Duis aute irure dolor in reprehenderit in", "{% if sections." + page_prefix + "_content %}{{ sections." + page_prefix + "_content.text|safe }}{% else %}Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat \n nulla pariatur Duis aute irure dolor in reprehenderit in{% endif %}")
        
        content = content.replace("Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur", "{% if sections." + page_prefix + "_short %}{{ sections." + page_prefix + "_short.text|safe }}{% else %}Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur{% endif %}")
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated headers in {filename}")

update_templates()
