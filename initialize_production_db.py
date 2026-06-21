import os
import django
import subprocess

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lebari_project.settings')
django.setup()

from django.core.management import call_command
from core.models import SiteSetting, HomePageSetting, AboutPageSetting, ContactPageSetting, CoursesPageSetting, BlogPageSetting

def main():
    print("Step 1: Running migrations to create new tables...")
    try:
        call_command('migrate')
        print("[OK] Migrations completed successfully.")
    except Exception as e:
        print(f"[ERROR] Migrations failed: {e}")
        return

    print("\nStep 2: Initializing default Page Settings if they do not exist...")
    
    # 1. SiteSetting
    if not SiteSetting.objects.exists():
        SiteSetting.objects.create(
            email='contact@lebari.com',
            phone='+1 (800) 123-4567',
            address='123 Education Lane, NY 10001, USA',
            logo_type='image'
        )
        print("[OK] Created default SiteSetting.")
    else:
        print("[OK] SiteSetting already exists.")

    # 2. HomePageSetting
    if not HomePageSetting.objects.exists():
        HomePageSetting.objects.create(
            hero_title="Empower Your Future with Online Education",
            hero_subtitle="Learn from the best industry experts and advance your career today.",
            hero_button_text="Browse Courses",
            hero_button_link="/courses/",
            instructor_title="Become an Instructor",
            instructor_text="Top instructors from around the world teach millions of students on LeBari.",
            instructor_button_text="Click here to apply",
            instructor_button_link="/membership/",
            professional_title="Start Learning from Professional Instructors",
            professional_subtitle="Professional Education",
            professional_text="Access highly curated and structured online learning resources.",
            professional_button_text="Browse All Courses",
            professional_button_link="/courses/",
            explore_courses_title="Explore Featured Courses",
            explore_courses_text="Learn anything at your own pace from industry leaders.",
            events_title="Upcoming Educational Events",
            events_subtitle="Events & Webinars",
            testimonials_title="What Our Successful Students Say",
            testimonials_subtitle="Student Testimonials",
            testimonials_text="Read stories and feedback from learners around the globe.",
            goal_title="Achieve Your Personal & Professional Goals",
            goal_subtitle="Achieve Goals",
            goal_text="Join a community of learners dedicated to self-improvement."
        )
        print("[OK] Created default HomePageSetting.")
    else:
        print("[OK] HomePageSetting already exists.")

    # 3. AboutPageSetting
    if not AboutPageSetting.objects.exists():
        AboutPageSetting.objects.create(
            banner_title="About Our Platform",
            banner_subtitle="Empowering learners worldwide through quality education.",
            goal_title="Start to Success",
            goal_subtitle="Achieve Goals",
            goal_text="We help you build the skills you need to achieve your career objectives."
        )
        print("[OK] Created default AboutPageSetting.")
    else:
        print("[OK] AboutPageSetting already exists.")

    # 4. ContactPageSetting
    if not ContactPageSetting.objects.exists():
        ContactPageSetting.objects.create(
            banner_title="Get In Touch With Us",
            banner_text="Have questions? Reach out to our support team and we will get back to you.",
            form_section_title="Send Us a Message",
            form_section_text="Fill out the contact form below and let us know how we can help you."
        )
        print("[OK] Created default ContactPageSetting.")
    else:
        print("[OK] ContactPageSetting already exists.")

    # 5. CoursesPageSetting
    if not CoursesPageSetting.objects.exists():
        CoursesPageSetting.objects.create(
            banner_title="Explore Our Courses",
            banner_text="Choose from our wide selection of professional courses."
        )
        print("[OK] Created default CoursesPageSetting.")
    else:
        print("[OK] CoursesPageSetting already exists.")

    # 6. BlogPageSetting
    if not BlogPageSetting.objects.exists():
        BlogPageSetting.objects.create(
            banner_title="Our Latest Articles & News",
            banner_text="Stay updated with the latest educational articles, insights, and stories."
        )
        print("[OK] Created default BlogPageSetting.")
    else:
        print("[OK] BlogPageSetting already exists.")

    print("\nStep 3: Running standard population scripts...")
    scripts = [
        'populate_all.py',
        'populate_footer.py',
        'populate_labels.py',
        'populate_menus.py',
        'populate_skills.py'
    ]

    for script in scripts:
        print(f"Running {script}...")
        try:
            res = subprocess.run(['python', script], capture_output=True, text=True)
            if res.returncode == 0:
                print(f"  [OK] {script} executed successfully.")
            else:
                print(f"  [WARNING] {script} exited with error code {res.returncode}.")
                print(f"  Error details: {res.stderr.strip()}")
        except Exception as e:
            print(f"  [ERROR] Could not execute {script}: {e}")

    print("\nAll production database initialization tasks are completed successfully!")

if __name__ == '__main__':
    main()
