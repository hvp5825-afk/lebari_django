from django.db import models

class SiteSetting(models.Model):
    LOGO_CHOICES = [
        ('image', 'Image Logo'),
        ('text', 'Text Logo'),
    ]
    logo_type = models.CharField(max_length=10, choices=LOGO_CHOICES, default='image')
    logo = models.ImageField(upload_to='settings/', blank=True, null=True)
    logo_text = models.CharField(max_length=100, blank=True, null=True, help_text="Text to display if Logo Type is 'Text Logo'")
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    opening_hours = models.CharField(max_length=255, blank=True, null=True, help_text="e.g. Week Days: 09.00 to 18.00 Sunday: Closed")
    map_url = models.URLField(blank=True, null=True, help_text="Google Maps Embed URL")
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    pinterest_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Site Settings"

class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True, help_text="Extra paragraph text for the banner")
    image = models.ImageField(upload_to='banners/')
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teachers/')

    def __str__(self):
        return self.name

class FAQ(models.Model):
    CATEGORY_CHOICES = [
        ('primary', 'Primary FAQ'),
        ('other', 'Other Questions'),
    ]
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='primary')

    def __str__(self):
        return self.question

class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/')
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title

class FrontendSection(models.Model):
    name = models.CharField(max_length=100, help_text="Internal name, e.g., 'Home 1 About'")
    identifier = models.CharField(max_length=50, unique=True, help_text="e.g., 'home1_about'")
    title = models.CharField(max_length=200, blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    extra_text = models.CharField(max_length=200, blank=True, null=True, help_text="e.g. Badge text or secondary subtitle")
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='frontend/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='frontend/', blank=True, null=True, help_text="Secondary image if needed")
    image_3 = models.ImageField(upload_to='frontend/', blank=True, null=True, help_text="Tertiary image if needed")
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class FeatureItem(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="e.g., 'flaticon-verify'")
    page = models.CharField(max_length=50, help_text="e.g., 'home1_services'", default='home1')

    def __str__(self):
        return f"{self.page} - {self.title}"

class CounterItem(models.Model):
    number = models.CharField(max_length=20, help_text="e.g., '36' or '15'")
    suffix = models.CharField(max_length=10, blank=True, null=True, help_text="e.g., '+' or 'k'")
    title = models.CharField(max_length=100)
    delay = models.CharField(max_length=20, default="0ms")

    def __str__(self):
        return self.title

class ClientLogo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name

class CustomPage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="e.g., 'abc' for '/abc/'")
    banner_image = models.ImageField(upload_to='custom_pages/', blank=True, null=True)
    content = models.TextField(help_text="HTML content for the page")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MembershipPlan(models.Model):
    CYCLE_CHOICES = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20, help_text="e.g. '$09', 'Free'")
    duration = models.CharField(max_length=20, help_text="e.g. '/month', '/year'")
    billing_cycle = models.CharField(max_length=10, choices=CYCLE_CHOICES, default='monthly')
    features = models.TextField(help_text="Enter one feature per line")
    is_featured = models.BooleanField(default=False, help_text="Highlight this plan (e.g. Enterprise)")
    button_text = models.CharField(max_length=50, default="Get started")
    button_link = models.CharField(max_length=200, default="#")

    def __str__(self):
        return f"{self.name} ({self.get_billing_cycle_display()})"

    def get_features_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]

class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.CharField(max_length=50)
    is_recurring = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True, default="Hi, I'm a new student here!")
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    pinterest_url = models.URLField(blank=True, null=True)
    dribbble_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class ButtonSetting(models.Model):
    identifier = models.CharField(max_length=50, unique=True, help_text="e.g. enroll_now, read_more, submit, subscribe")
    text = models.CharField(max_length=50, help_text="The actual text shown on the button")

    class Meta:
        verbose_name_plural = "Button Settings"

    def __str__(self):
        return f"{self.identifier} -> {self.text}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
    else:
        UserProfile.objects.create(user=instance)

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
