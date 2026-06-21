import os
import glob
import re

template_dir = 'templates'
html_files = glob.glob(os.path.join(template_dir, '*.html'))

replacements = [
    # Footer
    (r'(<h4[^>]*>)\s*Newsletter\s*(</h4>)', r'\1{{ labels.footer_newsletter_title|default:"Newsletter" }}\2'),
    (r'(<div class="text">)\s*Get started now and take advantage of our 30 day free trial today.\s*(</div>)', r'\1{{ labels.footer_newsletter_desc|default:"Get started now and take advantage of our 30 day free trial today." }}\2'),
    (r'placeholder="Your email"', r'placeholder="{{ labels.footer_email_placeholder|default:\'Your email\' }}"'),
    
    # Buttons
    (r'(<button[^>]*>)\s*Subscribe\s*(</button>)', r'\1{{ labels.footer_subscribe_btn|default:"Subscribe" }}\2'),
    (r'(<button[^>]*>)\s*Submit\s*(</button>)', r'\1{{ labels.form_submit_btn|default:"Submit" }}\2'),
    (r'(<button[^>]*type="submit"[^>]*>)\s*Submit\s*(</button>)', r'\1{{ labels.form_submit_btn|default:"Submit" }}\2'),
    
    # Course Page Sidebar
    (r'(<div class="widget-title">)\s*<h4>Filter</h4>\s*(</div>)', r'\1<h4>{{ labels.course_filter_title|default:"Filter" }}</h4>\2'),
    (r'(<div class="widget-title">)\s*<h4>Categories</h4>\s*(</div>)', r'\1<h4>{{ labels.course_categories_title|default:"Categories" }}</h4>\2'),
    (r'(<div class="widget-title">)\s*<h4>Instructor</h4>\s*(</div>)', r'\1<h4>{{ labels.course_instructor_title|default:"Instructor" }}</h4>\2'),
    (r'(<div class="widget-title">)\s*<h4>Price</h4>\s*(</div>)', r'\1<h4>{{ labels.course_price_title|default:"Price" }}</h4>\2'),
    (r'(<div class="widget-title">)\s*<h4>Level</h4>\s*(</div>)', r'\1<h4>{{ labels.course_level_title|default:"Level" }}</h4>\2'),
    (r'(<div class="widget-title">)\s*<h4>Language</h4>\s*(</div>)', r'\1<h4>{{ labels.course_language_title|default:"Language" }}</h4>\2'),
    (r'(<div class="widget-title">)\s*<h4>Duration</h4>\s*(</div>)', r'\1<h4>{{ labels.course_duration_title|default:"Duration" }}</h4>\2'),
    
    # Course Detail Tabs
    (r'(<li class="tab-btn active-btn" data-tab="#prod-description">)\s*Description\s*(</li>)', r'\1{{ labels.course_tab_description|default:"Description" }}\2'),
    (r'(<li class="tab-btn" data-tab="#prod-curriculum">)\s*Curriculum\s*(</li>)', r'\1{{ labels.course_tab_curriculum|default:"Curriculum" }}\2'),
    (r'(<li class="tab-btn" data-tab="#prod-reviews">)\s*Reviews\s*(</li>)', r'\1{{ labels.course_tab_reviews|default:"Reviews" }}\2'),
    (r'(<span class="share-title">)\s*Share:\s*(</span>)', r'\1{{ labels.course_share_title|default:"Share" }}:\2'),
    
    # Blog Page
    (r'(<div class="widget-title">)\s*<h4>Tags</h4>\s*(</div>)', r'\1<h4>{{ labels.blog_tags_title|default:"Tags" }}</h4>\2'),
    (r'(<div class="widget-title">)\s*<h4>Recent Posts</h4>\s*(</div>)', r'\1<h4>{{ labels.blog_recent_posts_title|default:"Recent Posts" }}</h4>\2'),
    (r'(<div class="group-title">)\s*<h4>Leave a Reply</h4>\s*(</div>)', r'\1<h4>{{ labels.blog_leave_reply_title|default:"Leave a Reply" }}</h4>\2'),
]

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")

print("Template replacement complete.")
