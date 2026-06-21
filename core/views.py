from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SiteSetting, Banner, Testimonial, Teacher, FAQ, Event, FrontendSection, FeatureItem, CounterItem, ClientLogo, HomePageSetting, AboutPageSetting, ContactPageSetting, CoursesPageSetting, BlogPageSetting, BlogPageSetting
from courses.models import Course, CourseCategory
from blog.models import Post

def get_cms_context(page_name=None):
    ctx = {
        'site_setting': SiteSetting.objects.first(),
        'sections': {s.key: s for s in FrontendSection.objects.all()},
        'testimonials': Testimonial.objects.filter(is_active=True).order_by('-created_at')
    }
    
    if page_name == 'home':
        ctx['home_page'] = HomePageSetting.objects.first()
    if page_name == 'about':
        ctx['about_page'] = AboutPageSetting.objects.first()
    if page_name == 'contact':
        ctx['contact_page'] = ContactPageSetting.objects.first()
    if page_name == 'course':
        ctx['course_page'] = CoursesPageSetting.objects.first()
    if page_name in ['blog_list', 'blog_detail']:
        ctx['blog_page'] = BlogPageSetting.objects.first()
    return ctx

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SiteSetting, Banner, Testimonial, Teacher, FAQ, Event, FrontendSection, FeatureItem, CounterItem, ClientLogo, HomePageSetting, AboutPageSetting, ContactPageSetting, CoursesPageSetting, BlogPageSetting
from courses.models import Course, CourseCategory
from blog.models import Post

def get_cms_context(page_name):
    sections = {s.identifier: s for s in FrontendSection.objects.all()}
    features = FeatureItem.objects.filter(page=page_name)
    counters = CounterItem.objects.all()
    clients = ClientLogo.objects.all()
    posts = Post.objects.all().order_by('-created_at')[:3]
    testimonials = Testimonial.objects.all()
    coursespage = CoursesPageSetting.objects.first()
    blogpage = BlogPageSetting.objects.first()
    return {'sections': sections, 'features': features, 'counters': counters, 'clients': clients, 'posts': posts, 'testimonials': testimonials, 'coursespage': coursespage, 'blogpage': blogpage}

def index(request):
    settings = SiteSetting.objects.first()
    homepage = HomePageSetting.objects.first()
    banners = Banner.objects.all()
    testimonials = Testimonial.objects.all()
    courses = Course.objects.all().order_by('-created_at')[:3]
    event = Event.objects.order_by('-date').first()
    
    ctx = {
        'settings': settings,
        'homepage': homepage,
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
    ctx = {
        'settings': settings,
    }
    ctx.update(get_cms_context('coaching'))
    return render(request, 'index-3.html', ctx)

def kindergarten(request):
    settings = SiteSetting.objects.first()
    ctx = {
        'settings': settings,
    }
    ctx.update(get_cms_context('kindergarten'))
    return render(request, 'index-4.html', ctx)

def university(request):
    settings = SiteSetting.objects.first()
    ctx = {
        'settings': settings,
    }
    ctx.update(get_cms_context('university'))
    return render(request, 'index-5.html', ctx)

def about(request):
    settings = SiteSetting.objects.first()
    aboutpage = AboutPageSetting.objects.first()
    from courses.models import Teacher
    from core.models import Testimonial
    ctx = {
        'settings': settings,
        'aboutpage': aboutpage,
        'teachers': Teacher.objects.all()[:4],
        'testimonials': Testimonial.objects.all(),
    }
    ctx.update(get_cms_context('about'))
    return render(request, 'about.html', ctx)

def contact(request):
    settings = SiteSetting.objects.first()
    contactpage = ContactPageSetting.objects.first()
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
        'contactpage': contactpage,
    })

def teacher_list(request):
    settings = SiteSetting.objects.first()
    teachers = Teacher.objects.all()
    ctx = {
        'settings': settings,
        'teachers': teachers,
    }
    ctx.update(get_cms_context('teacher'))
    return render(request, 'teacher.html', ctx)

def faq_list(request):
    settings = SiteSetting.objects.first()
    primary_faqs = FAQ.objects.filter(category='primary')
    other_faqs = FAQ.objects.filter(category='other')
    ctx = {
        'settings': settings,
        'primary_faqs': primary_faqs,
        'other_faqs': other_faqs,
    }
    ctx.update(get_cms_context('faq'))
    return render(request, 'faq.html', ctx)

def event_list(request):
    settings = SiteSetting.objects.first()
    events = Event.objects.all().order_by('-date')
    ctx = {
        'settings': settings,
        'events': events,
    }
    ctx.update(get_cms_context('event'))
    return render(request, 'event.html', ctx)

def event_detail(request, slug):
    settings = SiteSetting.objects.first()
    event = get_object_or_404(Event, slug=slug)
    recent_events = Event.objects.exclude(id=event.id).order_by('-date')[:3]
    return render(request, 'event-detail.html', {
        'settings': settings,
        'event': event,
        'recent_events': recent_events,
    })

from .models import MembershipPlan, Donation

def membership(request):
    settings = SiteSetting.objects.first()
    monthly_plans = MembershipPlan.objects.filter(billing_cycle='monthly')
    yearly_plans = MembershipPlan.objects.filter(billing_cycle='yearly')
    
    ctx = {
        'settings': settings,
        'monthly_plans': monthly_plans,
        'yearly_plans': yearly_plans,
    }
    ctx.update(get_cms_context('membership'))
    return render(request, 'membership.html', ctx)

def not_found(request, exception=None):
    settings = SiteSetting.objects.first()
    return render(request, 'not-found.html', {
        'settings': settings,
    })

def donation(request):
    settings = SiteSetting.objects.first()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount_radio = request.POST.get('payment-group')
        amount_text = request.POST.get('amount_text')
        
        amount = amount_text if amount_radio == 'Others' else amount_radio
        if not amount:
            amount = '$10'

        is_recurring = request.POST.get('is_recurring') == 'on'
        
        Donation.objects.create(
            name=name,
            email=email,
            amount=amount,
            is_recurring=is_recurring
        )
        messages.success(request, 'Thank you! Your donation request has been received.')
        return redirect('donation')

    ctx = {
        'settings': settings,
    }
    ctx.update(get_cms_context('donation'))
    return render(request, 'donation.html', ctx)


from django.contrib.auth.decorators import login_required
from courses.models import CourseEnrollment

@login_required(login_url='login')
def profile(request):
    settings = SiteSetting.objects.first()
    enrollments = CourseEnrollment.objects.filter(user=request.user)
    enrolled_count = enrollments.count()
    active_count = enrollments.filter(status='Active').count()
    completed_count = enrollments.filter(status='Completed').count()

    from .forms import UserUpdateForm, ProfileUpdateForm
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    ctx = {
        'settings': settings,
        'enrollments': enrollments,
        'enrolled_count': enrolled_count,
        'active_count': active_count,
        'completed_count': completed_count,
        'u_form': u_form,
        'p_form': p_form,
    }
    ctx.update(get_cms_context('profile'))
    return render(request, 'profile.html', ctx)
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

from .models import Subscriber

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(email=email)
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            else:
                messages.info(request, 'You are already subscribed to our newsletter!')
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    return redirect('index')
