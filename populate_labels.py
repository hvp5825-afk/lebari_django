import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lebari_project.settings')
django.setup()

from core.models import SiteLabel, ContactSubject

labels = {
    'about_form_subject_placeholder': 'When you want to start courses',
    'contact_form_name_placeholder': 'Name',
    'contact_form_email_placeholder': 'Email',
    'contact_form_subject_placeholder': 'Subject',
    'contact_form_message_placeholder': 'Comment',
    'contact_form_firstname': 'First Name',
    'contact_form_lastname': 'Last Name',
    'contact_form_date': 'Date',
    'contact_form_time': 'Time',
    'contact_form_comment': 'Type you comment here',
    'contact_form_submit': 'Submit',
    'faq_read_more_button': 'Read More',
    'faq_primary_title': 'Primary FAQ',
    'faq_other_title': 'Other questions',
    'teacher_contact_info_title': 'Contact us',
    'teacher_contact_info_text': 'It is a long established fact that a reader will be distracted by the readable content of a page',
    'teacher_contact_form_title': 'Visit us <br> for Free Resources',
    'teacher_contact_form_text': 'These leading universities are currently offering online degree courses on FutureLearn:',
    'login_form_title': 'Login to your account',
    'login_no_account_text': "Don't have an account?",
    'login_register_link': 'Register here',
    'register_form_title': 'Create an account',
    'register_has_account_text': 'Already have an account?',
    'register_login_link': 'Login here',
    'profile_enrolled_courses': 'Enrolled Courses',
    'profile_active_courses': 'Active Courses',
    'profile_completed_courses': 'Completed Courses',
    'profile_my_courses_title': 'My Courses',
    'profile_my_courses_text': 'Here are the courses you have enrolled in',
    'profile_no_courses': "You haven't enrolled in any courses yet.",
    'profile_browse_courses': 'Browse Courses'
}

for key, value in labels.items():
    obj, created = SiteLabel.objects.get_or_create(key=key, defaults={'value': value})
    if created:
        print(f"Created label: {key}")
    else:
        obj.value = value
        obj.save()
        print(f"Updated label: {key}")

subjects = [
    ('Web Development Course', 1),
    ('Graphic Design Course', 2),
    ('Data Science Bootcamp', 3),
    ('General Inquiry', 4)
]

for title, order in subjects:
    obj, created = ContactSubject.objects.get_or_create(title=title, defaults={'order': order})
    if created:
        print(f"Created subject: {title}")
    else:
        print(f"Subject exists: {title}")

print("Populated new labels and contact subjects!")
