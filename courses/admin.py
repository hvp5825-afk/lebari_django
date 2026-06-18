from django.contrib import admin
from .models import Teacher, CourseCategory, Course

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'teacher', 'price', 'rating')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'teacher')
    search_fields = ('title', 'description')

from .models import CourseModule, CourseLecture, CourseEnrollment, CourseReview

@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'status', 'enrolled_on')
    list_filter = ('status', 'course')

@admin.register(CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'created_at')
    list_filter = ('course',)

class CourseLectureInline(admin.TabularInline):
    model = CourseLecture
    extra = 1

@admin.register(CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'order')
    list_filter = ('course',)
    search_fields = ('title',)
    inlines = [CourseLectureInline]
