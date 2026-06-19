from django.shortcuts import render, get_object_or_404
from .models import Course, CourseCategory
from core.models import SiteSetting
from core.views import get_cms_context
def course_list(request):
    settings = SiteSetting.objects.first()
    query = request.GET.get('q')
    if query:
        courses = Course.objects.filter(title__icontains=query).order_by('-created_at')
    else:
        courses = Course.objects.all().order_by('-created_at')
    categories = CourseCategory.objects.all()
    ctx = {
        'settings': settings,
        'courses': courses,
        'categories': categories,
        'query': query,
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
