from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', RedirectView.as_view(url='/', permanent=True)),
    path('course.html', RedirectView.as_view(url='/courses/', permanent=True)),
    path('blog.html', RedirectView.as_view(url='/blog/', permanent=True)),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('faq.html', views.faq_list, name='faq'),
    path('teacher.html', views.teacher_list, name='teacher'),
    path('events/', views.event_list, name='event_list'),
    path('events/<slug:slug>/', views.event_detail, name='event_detail'),
    path('event.html', RedirectView.as_view(url='/events/', permanent=True)),
    path('membership/', views.membership, name='membership'),
    path('404/', views.not_found, name='not_found'),
    path('donation/', views.donation, name='donation'),
    path('profile/', views.profile, name='profile'),
    path('profile.html', RedirectView.as_view(url='/profile/', permanent=True)),
]
