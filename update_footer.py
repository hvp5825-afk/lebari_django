import os
import re

def update_footer(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The original footer has a <div class="row clearfix"> that contains 3 columns
    # We want to replace everything inside <div class="footer-column col-lg-7 col-md-12 col-sm-12"> <div class="row clearfix"> ... </div>
    # Actually, we can just replace the 3 <div class="column ..."> blocks
    
    old_pattern = r'<div class="row clearfix">\s*<div class="column col-lg-4 col-md-4 col-sm-12">.*?</div>\s*</div>'
    
    new_footer_html = '''<div class="row clearfix">
							{% for col in footer_columns %}
							<div class="column col-lg-4 col-md-4 col-sm-12">
								<h5>{{ col.title }}</h5>
								<ul class="list">
									{% for link in col.links.all %}
									<li><a href="{{ link.url }}">{{ link.title }}</a></li>
									{% endfor %}
								</ul>
							</div>
							{% endfor %}
						</div>'''

    if '<div class="footer-column col-lg-7' in content:
        # It's a bit tricky to replace exactly. Let's do a more precise replacement using split
        parts = content.split('<!-- Footer Column -->')
        if len(parts) > 2:
            # parts[2] is the second footer column
            sub_parts = parts[2].split('<!-- Lower Box -->')
            if len(sub_parts) > 1:
                footer_links_section = sub_parts[0]
                new_links_section = re.sub(
                    r'<div class="row clearfix">.*?</div>\s*</div>\s*</div>\s*</div>',
                    new_footer_html + '\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>',
                    footer_links_section,
                    flags=re.DOTALL
                )
                
                parts[2] = new_links_section + '<!-- Lower Box -->' + sub_parts[1]
                content = '<!-- Footer Column -->'.join(parts)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated footer in {filepath}")

update_footer('templates/base.html')
update_footer('templates/index-2.html')

