import os

template_path = 'templates/index-2.html'
with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 3. Instructor Section
content = content.replace(
    '{% if sections.home1_instructor %}{{ sections.home1_instructor.title }}{% else %}Become an instructor{% endif %}',
    '{{ homepage.instructor_title }}'
)
content = content.replace(
    '{% if sections.home1_instructor %}{{ sections.home1_instructor.text|safe }}{% else %}Top instructors from around the world teach millions of students Duis aute irure dolor in <br> voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non{% endif %}',
    '{{ homepage.instructor_text|safe }}'
)
content = content.replace(
    '{% if sections.home1_instructor %}{{ sections.home1_instructor.button_link }}{% else %}{% url \'membership\' %}{% endif %}',
    '{{ homepage.instructor_button_link }}'
)
content = content.replace(
    '{% if sections.home1_instructor %}{{ sections.home1_instructor.button_text }}{% else %}Click here for apply{% endif %}',
    '{{ homepage.instructor_button_text }}'
)
content = content.replace(
    '{% if sections.home1_instructor and sections.home1_instructor.image %}{{ sections.home1_instructor.image.url }}{% else %}{% static \'images/resource/instructor.png\' %}{% endif %}',
    '{% if homepage and homepage.instructor_image %}{{ homepage.instructor_image.url }}{% else %}{% static \'images/resource/instructor.png\' %}{% endif %}'
)

# 4. Professional Section
content = content.replace(
    '{% if sections.home2_professional %}{{ sections.home2_professional.subtitle }}{% else %}Learn anything{% endif %}',
    '{{ homepage.professional_subtitle }}'
)
content = content.replace(
    '{% if sections.home2_professional %}{{ sections.home2_professional.title|safe }}{% else %}Take online courses Earn <br> professional{% endif %}',
    '{{ homepage.professional_title|safe }}'
)
content = content.replace(
    '{% if sections.home2_professional %}{{ sections.home2_professional.text|safe }}{% else %}Position yourself for success with a variety of collegeclasses including general education courses{% endif %}',
    '{{ homepage.professional_text|safe }}'
)
content = content.replace(
    '{% if sections.home2_professional %}{{ sections.home2_professional.button_link }}{% else %}#{% endif %}',
    '{{ homepage.professional_button_link }}'
)
content = content.replace(
    '{% if sections.home2_professional %}{{ sections.home2_professional.button_text }}{% else %}Short courses{% endif %}',
    '{{ homepage.professional_button_text }}'
)
content = content.replace(
    '{% if sections.home2_professional and sections.home2_professional.image %}{{ sections.home2_professional.image.url }}{% else %}{% static \'images/resource/professional.jpg\' %}{% endif %}',
    '{% if homepage and homepage.professional_image %}{{ homepage.professional_image.url }}{% else %}{% static \'images/resource/professional.jpg\' %}{% endif %}'
)

# 5. Explore Courses Section
content = content.replace(
    '{% if sections.home_explore_courses %}{{ sections.home_explore_courses.title|safe }}{% else %}You can learn anything, Explore <br> featured courses{% endif %}',
    '{{ homepage.explore_courses_title|safe }}'
)
content = content.replace(
    '{% if sections.home_explore_courses %}{{ sections.home_explore_courses.text|safe }}{% else %}Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat <br> nulla pariatur Duis aute irure dolor in reprehenderit in{% endif %}',
    '{{ homepage.explore_courses_text|safe }}'
)

# 6. Events Section
content = content.replace(
    '{% if sections.home_events_section %}{{ sections.home_events_section.subtitle }}{% else %}Explore Event{% endif %}',
    '{{ homepage.events_subtitle }}'
)
content = content.replace(
    '{% if event %}{{ event.title }}{% elif sections.home_events_section %}{{ sections.home_events_section.title|safe }}{% else %}Our Upcoming Events{% endif %}',
    '{% if event %}{{ event.title }}{% else %}{{ homepage.events_title|safe }}{% endif %}'
)

# 7. Testimonials Section
content = content.replace(
    '{% if sections.index_2_testimonials %}{{ sections.index_2_testimonials.subtitle }}{% else %}Testimonial{% endif %}',
    '{{ homepage.testimonials_subtitle }}'
)
content = content.replace(
    '{% if sections.index_2_testimonials %}{{ sections.index_2_testimonials.title|safe }}{% else %}Words From Customers{% endif %}',
    '{{ homepage.testimonials_title|safe }}'
)
content = content.replace(
    '{% if sections.index_2_testimonials %}{{ sections.index_2_testimonials.text|safe }}{% else %}Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu <br> fugiat nulla pariatur Duis aute irure dolor in reprehenderit in{% endif %}',
    '{{ homepage.testimonials_text|safe }}'
)

# 8. Goal Section
content = content.replace(
    '{% if sections.home2_goal %}{{ sections.home2_goal.subtitle }}{% else %}Achieve Goals{% endif %}',
    '{{ homepage.goal_subtitle }}'
)
content = content.replace(
    '{% if sections.home2_goal %}{{ sections.home2_goal.title|safe }}{% else %}Start To Success{% endif %}',
    '{{ homepage.goal_title|safe }}'
)
content = content.replace(
    '{% if sections.home2_goal %}{{ sections.home2_goal.text|safe }}{% else %}{% if sections.index_2_short %}{{ sections.index_2_short.text|safe }}{% else %}Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur{% endif %} Duis aute irure dolor in{% endif %}',
    '{{ homepage.goal_text|safe }}'
)
content = content.replace(
    '{% if sections.home2_goal and sections.home2_goal.image %}{{ sections.home2_goal.image.url }}{% else %}{% static \'images/resource/goal-1.jpg\' %}{% endif %}',
    '{% if homepage and homepage.goal_image_1 %}{{ homepage.goal_image_1.url }}{% else %}{% static \'images/resource/goal-1.jpg\' %}{% endif %}'
)
content = content.replace(
    '{% if sections.home2_goal and sections.home2_goal.image_2 %}{{ sections.home2_goal.image_2.url }}{% else %}{% static \'images/resource/goal-2.jpg\' %}{% endif %}',
    '{% if homepage and homepage.goal_image_2 %}{{ homepage.goal_image_2.url }}{% else %}{% static \'images/resource/goal-2.jpg\' %}{% endif %}'
)

with open(template_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Template index-2.html deeply updated successfully!")
