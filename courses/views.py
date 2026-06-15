from django.shortcuts import render, get_object_or_404
from .models import Course, CourseCategory
from core.models import SiteSetting

def course_list(request):
    settings = SiteSetting.objects.first()
    courses = Course.objects.all().order_by('-created_at')
    categories = CourseCategory.objects.all()
    return render(request, 'course.html', {
        'settings': settings,
        'courses': courses,
        'categories': categories,
    })

def course_detail(request, slug):
    settings = SiteSetting.objects.first()
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'course-detail.html', {
        'settings': settings,
        'course': course,
    })
