from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='teachers/')
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class CourseCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='courses')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='courses')
    image = models.ImageField(upload_to='courses/')
    description = models.TextField()
    what_you_will_learn = models.TextField(blank=True, null=True, help_text="Comma or newline separated list of things students will learn")
    requirements = models.TextField(blank=True, null=True, help_text="Comma or newline separated list of requirements")
    includes = models.TextField(blank=True, null=True, help_text="Comma or newline separated list of what the course includes")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    original_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    duration = models.CharField(max_length=50, help_text="e.g. 11.5 total hours")
    level = models.CharField(max_length=50, help_text="e.g. All Levels")
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=5.0)
    reviews_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    side_text = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. 5 lectures . 5 video")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class CourseLecture(models.Model):
    module = models.ForeignKey(CourseModule, on_delete=models.CASCADE, related_name='lectures')
    title = models.CharField(max_length=200)
    time = models.CharField(max_length=50, blank=True, null=True, help_text="e.g. 10:25")
    icon_class = models.CharField(max_length=50, default="fa-play-circle-o", help_text="e.g. fa-play-circle-o, fa-file-o, fa-file-word-o")
    link = models.CharField(max_length=500, default="#", help_text="YouTube URL or # for document")
    is_lightbox = models.BooleanField(default=True, help_text="Check if this is a video that should open in a popup")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

from django.contrib.auth.models import User

class CourseEnrollment(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

class CourseReview(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.name} on {self.course.title}"
