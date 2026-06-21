import os

template_path = 'templates/index-2.html'
with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Hero Banner
content = content.replace(
    '{% if sections.home_hero_banner %}{{ sections.home_hero_banner.subtitle }}{% else %}Learn latest skills{% endif %}',
    '{{ homepage.hero_subtitle }}'
)
content = content.replace(
    '{% if sections.home_hero_banner %}{{ sections.home_hero_banner.title|safe }}{% else %}Build skills with <br> courses flexible online <br> courses{% endif %}',
    '{{ homepage.hero_title|safe }}'
)
content = content.replace(
    '{% if sections.home_hero_banner %}{{ sections.home_hero_banner.button_link }}{% else %}{% url \'about\' %}{% endif %}',
    '{{ homepage.hero_button_link }}'
)
content = content.replace(
    '{% if sections.home_hero_banner %}{{ sections.home_hero_banner.button_text }}{% else %}Join For free{% endif %}',
    '{{ homepage.hero_button_text }}'
)
content = content.replace(
    '{% if sections.home_hero_banner and sections.home_hero_banner.image %}{{ sections.home_hero_banner.image.url }}{% else %}{% static \'images/main-slider/image-5.png\' %}{% endif %}',
    '{% if homepage and homepage.hero_image %}{{ homepage.hero_image.url }}{% else %}{% static \'images/main-slider/image-5.png\' %}{% endif %}'
)

# About / Instructor
content = content.replace(
    '{% if sections.home_instructor %}{{ sections.home_instructor.title|safe }}{% else %}We Are Top <br> Online <span class="theme_color">Courses</span>{% endif %}',
    '{{ homepage.about_heading|safe }}'
)
content = content.replace(
    '{% if sections.home_instructor %}{{ sections.home_instructor.text|safe }}{% else %}<p class="text">The argument in favor of using filler text goes something like this: If you use real content in the Consulting Process, anytime you reach a review point you’ll end up reviewing and negotiating the content itself and not the design.</p>{% endif %}',
    '{{ homepage.about_text|safe }}'
)
content = content.replace(
    '{% if sections.home_instructor %}{{ sections.home_instructor.button_link }}{% else %}#{% endif %}',
    '{{ homepage.about_button_link }}'
)
content = content.replace(
    '{% if sections.home_instructor %}{{ sections.home_instructor.button_text }}{% else %}Discover More{% endif %}',
    '{{ homepage.about_button_text }}'
)

# Video
content = content.replace(
    '{% if sections.home_video %}{{ sections.home_video.title|safe }}{% else %}Explore Our <span class="theme_color">Video</span>{% endif %}',
    '{{ homepage.video_heading|safe }}'
)
content = content.replace(
    '{% if sections.home_video %}{{ sections.home_video.subtitle }}{% else %}Explore Online Courses{% endif %}',
    '{{ homepage.video_subheading }}'
)
content = content.replace(
    '{% if sections.home_video %}{{ sections.home_video.button_link }}{% else %}https://www.youtube.com/watch?v=kxPCFljwJws{% endif %}',
    '{{ homepage.video_url }}'
)
content = content.replace(
    '{% if sections.home_video and sections.home_video.image %}{{ sections.home_video.image.url }}{% else %}{% static \'images/background/3.jpg\' %}{% endif %}',
    '{% if homepage and homepage.video_bg_image %}{{ homepage.video_bg_image.url }}{% else %}{% static \'images/background/3.jpg\' %}{% endif %}'
)

# Pricing
content = content.replace(
    '{% if sections.home_pricing %}{{ sections.home_pricing.title|safe }}{% else %}Simple <span class="theme_color">Pricing</span>{% endif %}',
    '{{ homepage.pricing_heading|safe }}'
)
content = content.replace(
    '{% if sections.home_pricing %}{{ sections.home_pricing.subtitle }}{% else %}Pricing Package{% endif %}',
    '{{ homepage.pricing_subheading }}'
)

# CTA
content = content.replace(
    '{% if sections.home_cta %}{{ sections.home_cta.title|safe }}{% else %}We Are The <br> Best <span class="theme_color">Education</span>{% endif %}',
    '{{ homepage.cta_heading|safe }}'
)
content = content.replace(
    '{% if sections.home_cta %}{{ sections.home_cta.button_link }}{% else %}{% url \'about\' %}{% endif %}',
    '{{ homepage.cta_button_link }}'
)
content = content.replace(
    '{% if sections.home_cta %}{{ sections.home_cta.button_text }}{% else %}Register Now{% endif %}',
    '{{ homepage.cta_button_text }}'
)

with open(template_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Template index-2.html updated successfully!")
