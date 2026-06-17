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
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    pinterest_url = models.URLField(blank=True, null=True)

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
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='frontend/', blank=True, null=True)
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
