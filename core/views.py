from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SiteSetting, Banner, Testimonial, Teacher, FAQ, Event, FrontendSection, FeatureItem, CounterItem, ClientLogo
from courses.models import Course, CourseCategory
from blog.models import Post

def get_cms_context(page_name):
    sections = {s.identifier: s for s in FrontendSection.objects.all()}
    features = FeatureItem.objects.filter(page=page_name)
    counters = CounterItem.objects.all()
    clients = ClientLogo.objects.all()
    return {'sections': sections, 'features': features, 'counters': counters, 'clients': clients}

def index(request):
    settings = SiteSetting.objects.first()
    banners = Banner.objects.all()
    testimonials = Testimonial.objects.all()
    courses = Course.objects.all().order_by('-created_at')[:3]
    event = Event.objects.order_by('-date').first()
    
    ctx = {
        'settings': settings,
        'banners': banners,
        'testimonials': testimonials,
        'courses': courses,
        'event': event,
    }
    ctx.update(get_cms_context('home2'))
    return render(request, 'index-2.html', ctx)

def online_course_1(request):
    settings = SiteSetting.objects.first()
    banners = Banner.objects.all()
    testimonials = Testimonial.objects.all()
    courses = Course.objects.all().order_by('-created_at')[:3]
    posts = Post.objects.all().order_by('-created_at')[:2]
    
    ctx = {
        'settings': settings,
        'banners': banners,
        'testimonials': testimonials,
        'courses': courses,
        'posts': posts,
    }
    ctx.update(get_cms_context('home1'))
    return render(request, 'index.html', ctx)

def coaching(request):
    settings = SiteSetting.objects.first()
    return render(request, 'index-3.html', {
        'settings': settings,
    })

def kindergarten(request):
    settings = SiteSetting.objects.first()
    return render(request, 'index-4.html', {
        'settings': settings,
    })

def university(request):
    settings = SiteSetting.objects.first()
    return render(request, 'index-5.html', {
        'settings': settings,
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

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register_view(request):
    settings = SiteSetting.objects.first()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('index')
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form, 'settings': settings})

def login_view(request):
    settings = SiteSetting.objects.first()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request, f'You are now logged in as {user.username}.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'settings': settings})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('index')

from .models import CustomPage

def custom_page_detail(request, slug):
    settings = SiteSetting.objects.first()
    page = get_object_or_404(CustomPage, slug=slug, is_active=True)
    return render(request, 'custom_page.html', {
        'settings': settings,
        'page': page,
    })
