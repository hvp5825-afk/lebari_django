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


class HomePageSetting(models.Model):
    # Singleton setup
    class Meta:
        verbose_name = 'Home Page Setting'
        verbose_name_plural = 'Home Page Settings'
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        pass

    # 1. Hero Banner
    hero_title = models.CharField(max_length=255, default='Build skills with courses flexible online courses', help_text='Use <br> for line breaks')
    hero_subtitle = models.CharField(max_length=255, default='Learn latest skills')
    hero_button_text = models.CharField(max_length=50, default='Join For free')
    hero_button_link = models.CharField(max_length=255, default='/about/')
    hero_image = models.ImageField(upload_to='home/', null=True, blank=True)

    # 2. About / Instructor Section (Top sidebar about)
    about_heading = models.CharField(max_length=255, default='We Are Top <br> Online <span class="theme_color">Courses</span>')
    about_text = models.TextField(default="The argument in favor of using filler text goes something like this: If you use real content in the Consulting Process, anytime you reach a review point you'll end up reviewing and negotiating the content itself and not the design.")
    about_button_text = models.CharField(max_length=50, default='Discover More')
    about_button_link = models.CharField(max_length=255, default='/about/')
    about_image = models.ImageField(upload_to='home/', null=True, blank=True)
    
    # 3. Instructor Section (Become an instructor)
    instructor_title = models.CharField(max_length=255, default='Become an instructor')
    instructor_text = models.TextField(default='Top instructors from around the world teach millions of students Duis aute irure dolor in <br> voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non')
    instructor_button_text = models.CharField(max_length=50, default='Click here for apply')
    instructor_button_link = models.CharField(max_length=255, default='/membership/')
    instructor_image = models.ImageField(upload_to='home/', null=True, blank=True)

    # 4. Professional Section (Learn anything)
    professional_subtitle = models.CharField(max_length=255, default='Learn anything')
    professional_title = models.CharField(max_length=255, default='Take online courses Earn <br> professional')
    professional_text = models.TextField(default='Position yourself for success with a variety of collegeclasses including general education courses')
    professional_button_text = models.CharField(max_length=50, default='Short courses')
    professional_button_link = models.CharField(max_length=255, default='#')
    professional_image = models.ImageField(upload_to='home/', null=True, blank=True)

    # 5. Explore Courses Section
    explore_courses_title = models.CharField(max_length=255, default='You can learn anything, Explore <br> featured courses')
    explore_courses_text = models.TextField(default='Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat <br> nulla pariatur Duis aute irure dolor in reprehenderit in')

    # 6. Events Section
    events_subtitle = models.CharField(max_length=255, default='Explore Event')
    events_title = models.CharField(max_length=255, default='Our Upcoming Events')
    
    # 7. Testimonials Section
    testimonials_subtitle = models.CharField(max_length=255, default='Testimonial')
    testimonials_title = models.CharField(max_length=255, default='Words From Customers')
    testimonials_text = models.TextField(default='Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu <br> fugiat nulla pariatur Duis aute irure dolor in reprehenderit in')

    # 8. Goal Section (Achieve Goals)
    goal_subtitle = models.CharField(max_length=255, default='Achieve Goals')
    goal_title = models.CharField(max_length=255, default='Start To Success')
    goal_text = models.TextField(default='Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Duis aute irure dolor in')
    goal_image_1 = models.ImageField(upload_to='home/', null=True, blank=True)
    goal_image_2 = models.ImageField(upload_to='home/', null=True, blank=True)

    # 9. Video Section
    video_heading = models.CharField(max_length=255, default='Explore Our <span class="theme_color">Video</span>')
    video_subheading = models.CharField(max_length=255, default='Explore Online Courses')
    video_url = models.URLField(default='https://www.youtube.com/watch?v=kxPCFljwJws')
    video_bg_image = models.ImageField(upload_to='home/', null=True, blank=True)

    # 10. Pricing Section
    pricing_heading = models.CharField(max_length=255, default='Simple <span class="theme_color">Pricing</span>')
    pricing_subheading = models.CharField(max_length=255, default='Pricing Package')

    # 11. CTA Section
    cta_heading = models.CharField(max_length=255, default='We Are The <br> Best <span class="theme_color">Education</span>')
    cta_button_text = models.CharField(max_length=50, default='Register Now')
    cta_button_link = models.CharField(max_length=255, default='/register/')

    def __str__(self):
        return 'Home Page Global Settings'




class AboutPageSetting(models.Model):
    class Meta:
        verbose_name = 'About Page Setting'
        verbose_name_plural = 'About Page Settings'
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        pass

    # 1. Banner
    banner_title = models.CharField(max_length=255, default='Our mission is to provide <br> a free Online <br> Courses and Class')
    banner_subtitle = models.CharField(max_length=255, default='About')
    banner_image = models.ImageField(upload_to='about/', null=True, blank=True)
    banner_image_2 = models.ImageField(upload_to='about/', null=True, blank=True)

    # 2. Goal Section
    goal_subtitle = models.CharField(max_length=255, default='Achieve Goals')
    goal_title = models.CharField(max_length=255, default='Start To Success')
    goal_text = models.TextField(default='Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Duis aute irure dolor in')
    goal_image = models.ImageField(upload_to='about/', null=True, blank=True)
    goal_image_2 = models.ImageField(upload_to='about/', null=True, blank=True)

    # 3. Skill Section
    skill_subtitle = models.CharField(max_length=255, default='Our Status valu')
    skill_title = models.CharField(max_length=255, default='Differentiate your classroom <br> What makes us special?')
    skill_text = models.TextField(default='Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur')
    skill_image = models.ImageField(upload_to='about/', null=True, blank=True)

    # 4. Professional Section
    professional_subtitle = models.CharField(max_length=255, default='Learn anything')
    professional_title = models.CharField(max_length=255, default='Take online courses Earn <br> professional')
    professional_text = models.TextField(default='Position yourself for success with a variety of collegeclasses including general education courses')
    professional_button_text = models.CharField(max_length=50, default='Short courses')
    professional_button_link = models.CharField(max_length=255, default='#')
    professional_image = models.ImageField(upload_to='about/', null=True, blank=True)

    # 5. Testimonial Section
    testimonials_subtitle = models.CharField(max_length=255, default='Testimonial')
    testimonials_title = models.CharField(max_length=255, default='Words From Customers')
    testimonials_text = models.TextField(default='Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu <br> fugiat nulla pariatur Duis aute irure dolor in reprehenderit in')

    # 6. Team Section
    team_title = models.CharField(max_length=255, default='Our best online Techer')
    team_text = models.TextField(default='Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur')
    team_button_text = models.CharField(max_length=50, default='View More')
    team_button_link = models.CharField(max_length=255, default='#')

    # 7. Clients Section
    clients_title = models.CharField(max_length=255, default='Key supporters')
    clients_text = models.TextField(default='These leading universities are currently offering online degree <br> courses on FutureLearn:')

    # 8. Contact Section
    contact_info_title = models.CharField(max_length=255, default='Contact us')
    contact_info_text = models.TextField(default='It is a long established fact that a reader will be distracted by the readable content of a page')
    contact_form_title = models.CharField(max_length=255, default='Visit us <br> for Free Resources')
    contact_form_text = models.TextField(default='These leading universities are currently offering online degree courses on FutureLearn:')

    def __str__(self):
        return 'About Page Global Settings'


class ContactPageSetting(models.Model):
    class Meta:
        verbose_name = 'Contact Page Setting'
        verbose_name_plural = 'Contact Page Settings'
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        pass

    # 1. Banner Section
    banner_subtitle = models.CharField(max_length=255, default='Contact us')
    banner_title = models.CharField(max_length=255, default='Contact Now')
    banner_text = models.TextField(default='Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Duis aute irure dolor in reprehenderit in')

    # 2. Info Section
    info_subtitle = models.CharField(max_length=255, default='GET IN TOUCH')
    info_title = models.CharField(max_length=255, default='Visit one of our agency locations <br> or contact us today')
    info_text = models.TextField(default='We\'d love to hear from you. Whether you have a question about our courses, pricing, or anything else, our team is ready to answer all your questions.')

    # 3. Form Section
    form_title = models.CharField(max_length=255, default='Leave a message')
    form_text = models.TextField(default='Please fill out the form below and we will get back to you as soon as possible.')
    form_button_text = models.CharField(max_length=50, default='Send Message')

    def __str__(self):
        return 'Contact Page Global Settings'

class CoursesPageSetting(models.Model):
    class Meta:
        verbose_name = 'Courses Page Setting'
        verbose_name_plural = 'Courses Page Settings'
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
        
    def delete(self, *args, **kwargs):
        pass

    # 1. Banner Section
    banner_subtitle = models.CharField(max_length=255, default='Courses v1')
    banner_title = models.CharField(max_length=255, default='Explore <br> Featured Courses')
    banner_image_1 = models.ImageField(upload_to='courses/', null=True, blank=True)
    banner_image_2 = models.ImageField(upload_to='courses/', null=True, blank=True)

    def __str__(self):
        return 'Courses Page Global Settings'

class BlogPageSetting(models.Model):
    banner_subtitle = models.CharField(max_length=200, default='Blog default')
    banner_title = models.CharField(max_length=200, default='Latest articles & news')
    banner_text = models.TextField(default='Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Duis aute irure dolor in reprehenderit in')
    button_text = models.CharField(max_length=50, default='View More Artical')
    button_link = models.CharField(max_length=255, default='#')
    default_post_image = models.ImageField(upload_to='blog/defaults/', null=True, blank=True, help_text='Fallback image for blog posts that do not have an image.')

    class Meta:
        verbose_name = 'Blog Page Setting'
        verbose_name_plural = 'Blog Page Settings'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
    
    def __str__(self):
        return 'Blog Page Setting'




class SiteLabel(models.Model):
    key = models.CharField(max_length=50, unique=True, help_text="Do not change this key once created, as it's used in HTML templates.")
    value = models.CharField(max_length=255, help_text="The actual text that will be displayed on the website.")
    description = models.CharField(max_length=255, blank=True, null=True, help_text="Where is this label used?")
    
    class Meta:
        verbose_name = 'Site Label & Text'
        verbose_name_plural = 'Site Labels & Texts'
        ordering = ['key']
        
    def __str__(self):
        return f"{self.key} : {self.value}"

class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200, help_text="e.g. '/' or '/about/'")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    order = models.IntegerField(default=0)
    is_auth_required = models.BooleanField(default=False, help_text="Show only to logged in users (e.g. Profile)")
    is_guest_only = models.BooleanField(default=False, help_text="Show only to logged out users (e.g. Login)")

    class Meta:
        ordering = ['order']
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    def __str__(self):
        if self.parent:
            return f"{self.parent.title} > {self.title}"
        return self.title

class FooterColumn(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Footer Column'
        verbose_name_plural = 'Footer Columns'

    def __str__(self):
        return self.title

class FooterLink(models.Model):
    column = models.ForeignKey(FooterColumn, on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Footer Link'
        verbose_name_plural = 'Footer Links'

    def __str__(self):
        return f"{self.column.title} > {self.title}"

class SkillBar(models.Model):
    title = models.CharField(max_length=100)
    percentage = models.IntegerField(help_text="Value between 0 and 100")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Skill Bar'
        verbose_name_plural = 'Skill Bars'

    def __str__(self):
        return f"{self.title} ({self.percentage}%)"

class ContactSubject(models.Model):
    title = models.CharField(max_length=200, help_text="e.g. 'Web Development Course' or 'General Inquiry'")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Contact Subject'
        verbose_name_plural = 'Contact Subjects'

    def __str__(self):
        return self.title
