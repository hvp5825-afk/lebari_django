from django.contrib import admin
from .models import SiteSetting, Banner, Testimonial, ContactMessage, Teacher, FAQ, Event

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'button_text')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category')
    list_filter = ('category',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time_start', 'time_end', 'location')
    prepopulated_fields = {'slug': ('title',)}

from .models import FrontendSection, FeatureItem, CounterItem, ClientLogo

@admin.register(FrontendSection)
class FrontendSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'identifier', 'title')

@admin.register(FeatureItem)
class FeatureItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'icon_class')
    list_filter = ('page',)

@admin.register(CounterItem)
class CounterItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'suffix')

@admin.register(ClientLogo)
class ClientLogoAdmin(admin.ModelAdmin):
    list_display = ('name',)

from .models import CustomPage

@admin.register(CustomPage)
class CustomPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_active',)
    search_fields = ('title', 'slug')
