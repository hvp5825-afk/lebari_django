from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SiteSetting, Banner, Testimonial, Teacher, FAQ, Event
from courses.models import Course, CourseCategory

def index(request):
    settings = SiteSetting.objects.first()
    banners = Banner.objects.all()
    testimonials = Testimonial.objects.all()
    # Get latest 3 courses for the homepage
    courses = Course.objects.all().order_by('-created_at')[:3]
    return render(request, 'index.html', {
        'settings': settings,
        'banners': banners,
        'testimonials': testimonials,
        'courses': courses,
    })

def about(request):
    settings = SiteSetting.objects.first()
    return render(request, 'about.html', {
        'settings': settings,
    })

def contact(request):
    settings = SiteSetting.objects.first()
    if request.method == 'POST':
        # Simple processing for contact form
        name = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            from .models import ContactMessage
            ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
            messages.success(request, 'Your message has been sent successfully!')
        elif email and not name:
            # Newsletter subscription fallback
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            
        referer = request.META.get('HTTP_REFERER')
        if referer:
            return redirect(referer)
        return redirect('contact')
        
    return render(request, 'contact.html', {
        'settings': settings,
    })

def teacher_list(request):
    settings = SiteSetting.objects.first()
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {
        'settings': settings,
        'teachers': teachers,
    })

def faq_list(request):
    settings = SiteSetting.objects.first()
    primary_faqs = FAQ.objects.filter(category='primary')
    other_faqs = FAQ.objects.filter(category='other')
    return render(request, 'faq.html', {
        'settings': settings,
        'primary_faqs': primary_faqs,
        'other_faqs': other_faqs,
    })

def event_list(request):
    settings = SiteSetting.objects.first()
    events = Event.objects.all().order_by('-date')
    return render(request, 'event.html', {
        'settings': settings,
        'events': events,
    })

def event_detail(request, slug):
    settings = SiteSetting.objects.first()
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'event-detail.html', {
        'settings': settings,
        'event': event,
    })

def membership(request):
    settings = SiteSetting.objects.first()
    return render(request, 'membership.html', {
        'settings': settings,
    })

def not_found(request, exception=None):
    settings = SiteSetting.objects.first()
    return render(request, 'not-found.html', {
        'settings': settings,
    })

def donation(request):
    settings = SiteSetting.objects.first()
    return render(request, 'donation.html', {
        'settings': settings,
    })


def profile(request):
    settings = SiteSetting.objects.first()
    return render(request, 'profile.html', {
        'settings': settings,
    })
