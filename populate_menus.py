import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lebari_project.settings")
django.setup()

from core.models import MenuItem

def run():
    MenuItem.objects.all().delete()
    
    # 1. Home
    MenuItem.objects.create(title="Home", url="/", order=10)
    
    # 2. About (Dropdown)
    about = MenuItem.objects.create(title="About", url="#", order=20)
    MenuItem.objects.create(title="About Us", url="/about.html", parent=about, order=10)
    MenuItem.objects.create(title="Faq", url="/faq.html", parent=about, order=20)
    MenuItem.objects.create(title="Teachers", url="/teacher.html", parent=about, order=30)
    MenuItem.objects.create(title="Membership", url="/membership/", parent=about, order=40)
    MenuItem.objects.create(title="Events", url="/events/", parent=about, order=50)

    # 3. Courses
    MenuItem.objects.create(title="Courses", url="/courses/", order=30)

    # 4. Blog
    MenuItem.objects.create(title="Blog", url="/blog/", order=40)

    # 5. Profile (Auth required, Dropdown)
    profile = MenuItem.objects.create(title="Profile", url="#", is_auth_required=True, order=50)
    MenuItem.objects.create(title="Dashboard", url="/profile/", parent=profile, order=10)
    MenuItem.objects.create(title="Logout", url="/logout/", parent=profile, order=20)

    # 6. Login / Register (Guest only)
    MenuItem.objects.create(title="Login / Register", url="/login/", is_guest_only=True, order=60)

    # 7. Contact
    MenuItem.objects.create(title="Contact", url="/contact.html", order=70)

    print("Menu populated!")

if __name__ == '__main__':
    run()
