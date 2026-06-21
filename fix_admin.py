with open('core/admin.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix CoursesPageSettingAdmin
content = content.replace(
    """class CoursesPageSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Banner Section', {
            'fields': ('banner_title', 'banner_subtitle', 'banner_text', 'button_text', 'button_link', 'default_post_image')
        }),
    )""",
    """class CoursesPageSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('1. Banner Section', {
            'fields': ('banner_subtitle', 'banner_title', 'banner_image_1', 'banner_image_2')
        }),
    )"""
)

# Add fieldsets to BlogPageSettingAdmin
content = content.replace(
    """class BlogPageSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):""",
    """class BlogPageSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Banner Section', {
            'fields': ('banner_title', 'banner_subtitle', 'banner_text', 'button_text', 'button_link', 'default_post_image')
        }),
    )

    def has_add_permission(self, request):"""
)

with open('core/admin.py', 'w', encoding='utf-8') as f:
    f.write(content)
