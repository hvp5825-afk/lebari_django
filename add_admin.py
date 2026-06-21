with open('core/admin.py', 'a', encoding='utf-8') as f:
    f.write('''

from .models import MenuLink, FooterColumn, FooterLink

@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent', 'order')
    list_editable = ('order',)
    list_filter = ('parent',)

class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1

@admin.register(FooterColumn)
class FooterColumnAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    inlines = [FooterLinkInline]
''')
