from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course-2.html', RedirectView.as_view(url='/courses/', permanent=True)),
    path('course-3.html', RedirectView.as_view(url='/courses/', permanent=True)),
    path('course-4.html', RedirectView.as_view(url='/courses/', permanent=True)),
    path('<slug:slug>/', views.course_detail, name='course_detail'),
]
