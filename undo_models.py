import os
import re

# Delete migration
try:
    os.remove('core/migrations/0023_footercolumn_footerlink_menulink.py')
    print("Deleted migration 0023")
except:
    pass

# Remove from models.py
with open('core/models.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'class MenuLink\(models\.Model\):.*?def __str__\(self\):\n\s*return f"\{self\.column\.title\} -> \{self\.title\}"\n', '', content, flags=re.DOTALL)
content = content.replace("from .models import MenuLink, FooterColumn", "")

with open('core/models.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Removed models from models.py")

# Remove from admin.py
with open('core/admin.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'from \.models import MenuLink, FooterColumn, FooterLink.*?inlines = \[FooterLinkInline\]\n', '', content, flags=re.DOTALL)

with open('core/admin.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Removed models from admin.py")
