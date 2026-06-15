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
