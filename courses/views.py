
from django.shortcuts import render, get_object_or_404
from .models import Course, CourseCategory, Teacher
from core.models import SiteSetting
from core.views import get_cms_context

def course_list(request):
    settings = SiteSetting.objects.first()
    courses = Course.objects.all().order_by('-created_at')
    
    query = request.GET.get('q')
    if query:
        courses = courses.filter(title__icontains=query)
        
    categories = request.GET.getlist('category')
    if categories:
        courses = courses.filter(category__id__in=categories)
        
    teachers = request.GET.getlist('teacher')
    if teachers:
        courses = courses.filter(teacher__id__in=teachers)
        
    prices = request.GET.getlist('price')
    if prices:
        if 'free' in prices and 'paid' in prices:
            pass # Show all
        elif 'free' in prices:
            courses = courses.filter(price=0)
        elif 'paid' in prices:
            courses = courses.filter(price__gt=0)
            
    levels = request.GET.getlist('level')
    if levels:
        courses = courses.filter(level__in=levels)
        
    sort = request.GET.get('sort')
    if sort == 'old':
        courses = courses.order_by('created_at')
    elif sort == 'new':
        courses = courses.order_by('-created_at')

    all_categories = CourseCategory.objects.all()
    all_teachers = Teacher.objects.all()
    
    ctx = {
        'settings': settings,
        'courses': courses,
        'categories': all_categories,
        'teachers': all_teachers,
        'query': query,
        'selected_categories': [int(c) for c in categories] if categories else [],
        'selected_teachers': [int(t) for t in teachers] if teachers else [],
        'selected_prices': prices,
        'selected_levels': levels,
        'selected_sort': sort,
    }
    ctx.update(get_cms_context('course'))
    return render(request, 'course.html', ctx)

def course_detail(request, slug):
    settings = SiteSetting.objects.first()
    course = get_object_or_404(Course, slug=slug)
    
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and message:
            from .models import CourseReview
            CourseReview.objects.create(
                course=course,
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            from django.contrib import messages
            messages.success(request, 'Your review has been submitted successfully.')
            from django.shortcuts import redirect
            return redirect('course_detail', slug=slug)

    is_enrolled = False
    if request.user.is_authenticated:
        from .models import CourseEnrollment
        is_enrolled = CourseEnrollment.objects.filter(user=request.user, course=course).exists()
        
    reviews = course.reviews.all().order_by('-created_at')

    ctx = {
        'settings': settings,
        'course': course,
        'is_enrolled': is_enrolled,
        'reviews': reviews,
    }
    ctx.update(get_cms_context('course_detail'))
    return render(request, 'course-detail.html', ctx)

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from .models import CourseEnrollment

@login_required(login_url='login')
def enroll_course(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = CourseEnrollment.objects.get_or_create(
        user=request.user,
        course=course,
        defaults={'status': 'Active'}
    )
    if created:
        messages.success(request, f"You have successfully enrolled in {course.title}!")
    else:
        messages.info(request, f"You are already enrolled in {course.title}.")
    return redirect('profile')
