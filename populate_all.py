import os
import django
from django.utils import timezone
from datetime import timedelta, datetime, time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lebari_project.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import SiteSetting, Banner, Testimonial, FAQ, Event, Teacher as CoreTeacher
from courses.models import Teacher as CourseTeacher, CourseCategory, Course
from blog.models import BlogCategory, Post

def populate():
    # 1. Get or Create Superuser for author
    admin_user, _ = User.objects.get_or_create(username='admin', defaults={'email': 'admin@lebari.com', 'is_superuser': True, 'is_staff': True})
    if not admin_user.password:
        admin_user.set_password('admin123')
        admin_user.save()

    # 2. Populate Site Settings
    SiteSetting.objects.get_or_create(
        id=1,
        defaults={
            'email': 'contact@lebari.com',
            'phone': '+1 (800) 123-4567',
            'address': '123 Education Lane, NY 10001, USA',
            'facebook_url': 'https://facebook.com',
            'twitter_url': 'https://twitter.com',
            'instagram_url': 'https://instagram.com'
        }
    )

    # 3. Populate Banners
    Banner.objects.get_or_create(
        title="Empower Your Future",
        subtitle="Learn from the best industry experts and advance your career today.",
        defaults={'button_text': 'Browse Courses', 'button_link': '/courses/'}
    )
    Banner.objects.get_or_create(
        title="Master New Skills",
        subtitle="Join our community of over 10,000 successful students worldwide.",
        defaults={'button_text': 'Join Now', 'button_link': '/register/'}
    )

    # 4. Populate FAQs
    faqs = [
        ("How do I enroll in a course?", "To enroll, simply navigate to the Courses page, select your desired course, and click 'Enroll Now'.", "Enrollment"),
        ("Are the courses self-paced?", "Yes, the majority of our online courses are self-paced, allowing you to learn at your own convenience.", "Learning"),
        ("Do I get a certificate?", "Absolutely! Upon successful completion of a course, you will receive a verifiable digital certificate.", "Certification")
    ]
    for q, a, c in faqs:
        FAQ.objects.get_or_create(question=q, defaults={'answer': a, 'category': c})

    # 5. Populate Testimonials
    Testimonial.objects.get_or_create(
        name="John Doe",
        defaults={'designation': "Web Developer", 'text': "This platform completely changed my career. The instructors are top-notch and the curriculum is very practical."}
    )
    Testimonial.objects.get_or_create(
        name="Jane Smith",
        defaults={'designation': "Data Analyst", 'text': "I learned so much in just a few weeks. The UI/UX course was brilliant and easy to follow."}
    )

    # 6. Populate Events
    Event.objects.get_or_create(
        title="Annual Tech Summit 2026",
        slug="tech-summit-2026",
        defaults={
            'date': timezone.now().date() + timedelta(days=30),
            'time_start': time(9, 0),
            'time_end': time(17, 0),
            'location': "Main Auditorium, NY Campus",
            'description': "Join us for our annual tech summit featuring industry leaders and workshops.",
            'content': "The tech summit will cover AI, Web Development, and Cyber Security. Networking lunch included."
        }
    )

    # 7. Populate Core Teachers (if not populated)
    CoreTeacher.objects.get_or_create(name="Emily Chen", defaults={'designation': "AI Specialist"})
    CoreTeacher.objects.get_or_create(name="Michael Brown", defaults={'designation': "Cyber Security Expert"})

    # 8. Populate Blog Categories and Posts
    bcat1, _ = BlogCategory.objects.get_or_create(name="Technology", slug="technology")
    bcat2, _ = BlogCategory.objects.get_or_create(name="Education", slug="education")

    Post.objects.get_or_create(
        title="The Future of AI in Education",
        slug="future-of-ai-education",
        defaults={
            'category': bcat1,
            'author': admin_user,
            'content': "Artificial Intelligence is rapidly changing how we learn. From personalized tutoring systems to automated grading, the possibilities are endless.",
            'created_at': timezone.now()
        }
    )
    Post.objects.get_or_create(
        title="Top 5 Study Habits for Online Learners",
        slug="study-habits-online",
        defaults={
            'category': bcat2,
            'author': admin_user,
            'content': "Online learning requires discipline. Set a schedule, create a dedicated workspace, and take regular breaks to maximize your retention.",
            'created_at': timezone.now()
        }
    )

    # 9. Additional Courses (to make it look full)
    CourseCategory.objects.get_or_create(name="Business", slug="business")
    c_teacher, _ = CourseTeacher.objects.get_or_create(name="David Clark", defaults={'designation': "Marketing Director", 'bio': "15 years of digital marketing experience."})
    c_cat = CourseCategory.objects.get(slug="business")

    Course.objects.get_or_create(
        title="Digital Marketing Masterclass",
        slug="digital-marketing-masterclass",
        defaults={
            'category': c_cat,
            'teacher': c_teacher,
            'price': 39.99,
            'original_price': 89.99,
            'duration': '15 Hours',
            'level': 'Intermediate',
            'rating': 4.7,
            'reviews_count': 320,
            'description': "Learn SEO, Social Media Marketing, and Google Ads from an industry expert."
        }
    )

    print("Successfully populated comprehensive dummy data across all backend models!")

if __name__ == '__main__':
    populate()
