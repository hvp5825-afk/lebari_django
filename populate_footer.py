import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lebari_project.settings")
django.setup()

from core.models import FooterColumn, FooterLink

def run():
    FooterColumn.objects.all().delete()

    # Column 1: About
    col1 = FooterColumn.objects.create(title="About", order=10)
    FooterLink.objects.create(column=col1, title="About Us", url="/about.html", order=10)
    FooterLink.objects.create(column=col1, title="News & Blog", url="/blog/", order=20)
    FooterLink.objects.create(column=col1, title="Our Team", url="/teacher.html", order=30)
    FooterLink.objects.create(column=col1, title="Contact Us", url="/contact.html", order=40)

    # Column 2: Need some help?
    col2 = FooterColumn.objects.create(title="Need some help?", order=20)
    FooterLink.objects.create(column=col2, title="FAQs", url="/faq.html", order=10)
    FooterLink.objects.create(column=col2, title="Help Centre", url="/contact.html", order=20)
    FooterLink.objects.create(column=col2, title="Create Account", url="/register/", order=30)
    FooterLink.objects.create(column=col2, title="Login", url="/login/", order=40)

    # Column 3: Links
    col3 = FooterColumn.objects.create(title="Links", order=30)
    FooterLink.objects.create(column=col3, title="All Courses", url="/courses/", order=10)
    FooterLink.objects.create(column=col3, title="Membership", url="/membership/", order=20)
    FooterLink.objects.create(column=col3, title="Events", url="/events/", order=30)
    FooterLink.objects.create(column=col3, title="Donation", url="/donation/", order=40)

    print("Footer columns populated!")

if __name__ == '__main__':
    run()
