from django.contrib import admin
from .models import SiteSetting, Banner, Testimonial, ContactMessage, Teacher, FAQ, Event, ButtonSetting, MenuItem, FooterColumn, FooterLink, SkillBar, ContactSubject

@admin.register(ButtonSetting)
class ButtonSettingAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'text')
    search_fields = ('identifier', 'text')

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

from .models import Subscriber

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)

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

from .models import MembershipPlan, Donation, UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'billing_cycle', 'is_featured')
    list_filter = ('billing_cycle', 'is_featured')

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'is_recurring', 'created_at')
    list_filter = ('is_recurring', 'created_at')
    readonly_fields = ('created_at',)


from .models import HomePageSetting

@admin.register(HomePageSetting)
class HomePageSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('1. Hero Banner', {
            'fields': ('hero_subtitle', 'hero_title', 'hero_button_text', 'hero_button_link', 'hero_image')
        }),
        ('2. About Section', {
            'fields': ('about_heading', 'about_text', 'about_button_text', 'about_button_link', 'about_image')
        }),
        ('3. Instructor Section', {
            'fields': ('instructor_title', 'instructor_text', 'instructor_button_text', 'instructor_button_link', 'instructor_image')
        }),
        ('4. Professional Section', {
            'fields': ('professional_subtitle', 'professional_title', 'professional_text', 'professional_button_text', 'professional_button_link', 'professional_image')
        }),
        ('5. Explore Courses Section', {
            'fields': ('explore_courses_title', 'explore_courses_text')
        }),
        ('6. Events Section', {
            'fields': ('events_subtitle', 'events_title')
        }),
        ('7. Testimonials Section', {
            'fields': ('testimonials_subtitle', 'testimonials_title', 'testimonials_text')
        }),
        ('8. Goal Section', {
            'fields': ('goal_subtitle', 'goal_title', 'goal_text', 'goal_image_1', 'goal_image_2')
        }),
        ('9. Video Section', {
            'fields': ('video_subheading', 'video_heading', 'video_url', 'video_bg_image')
        }),
        ('10. Pricing Section', {
            'fields': ('pricing_heading', 'pricing_subheading')
        }),
        ('11. Call To Action', {
            'fields': ('cta_heading', 'cta_button_text', 'cta_button_link')
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


from .models import AboutPageSetting

@admin.register(AboutPageSetting)
class AboutPageSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('1. Banner Section', {
            'fields': ('banner_subtitle', 'banner_title', 'banner_image', 'banner_image_2')
        }),
        ('2. Goal Section', {
            'fields': ('goal_subtitle', 'goal_title', 'goal_text', 'goal_image', 'goal_image_2')
        }),
        ('3. Skill Section', {
            'fields': ('skill_subtitle', 'skill_title', 'skill_text', 'skill_image')
        }),
        ('4. Professional Section', {
            'fields': ('professional_subtitle', 'professional_title', 'professional_text', 'professional_button_text', 'professional_button_link', 'professional_image')
        }),
        ('5. Testimonial Section', {
            'fields': ('testimonials_subtitle', 'testimonials_title', 'testimonials_text')
        }),
        ('6. Team Section', {
            'fields': ('team_title', 'team_text', 'team_button_text', 'team_button_link')
        }),
        ('7. Clients Section', {
            'fields': ('clients_title', 'clients_text')
        }),
        ('8. Contact Section', {
            'fields': ('contact_info_title', 'contact_info_text', 'contact_form_title', 'contact_form_text')
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


from .models import ContactPageSetting

@admin.register(ContactPageSetting)
class ContactPageSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('1. Banner Section', {
            'fields': ('banner_subtitle', 'banner_title', 'banner_text')
        }),
        ('2. Info Section', {
            'fields': ('info_subtitle', 'info_title', 'info_text')
        }),
        ('3. Form Section', {
            'fields': ('form_title', 'form_text', 'form_button_text')
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False



from .models import CoursesPageSetting

@admin.register(CoursesPageSetting)
class CoursesPageSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('1. Banner Section', {
            'fields': ('banner_subtitle', 'banner_title', 'banner_image_1', 'banner_image_2')
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

from .models import BlogPageSetting

@admin.register(BlogPageSetting)
class BlogPageSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Banner Section', {
            'fields': ('banner_title', 'banner_subtitle', 'banner_text', 'button_text', 'button_link', 'default_post_image')
        }),
    )

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False



from .models import SiteLabel

@admin.register(SiteLabel)
class SiteLabelAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'description')
    search_fields = ('key', 'value', 'description')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent', 'order', 'is_auth_required', 'is_guest_only')
    list_filter = ('is_auth_required', 'is_guest_only')
    search_fields = ('title', 'url')
    ordering = ('parent__order', 'parent__id', 'order')

class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1
    ordering = ('order',)

@admin.register(FooterColumn)
class FooterColumnAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    inlines = [FooterLinkInline]
    ordering = ('order',)

@admin.register(SkillBar)
class SkillBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'percentage', 'order')
    ordering = ('order',)

@admin.register(ContactSubject)
class ContactSubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)


