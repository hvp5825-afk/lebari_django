from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('detail/', views.default_blog_detail, name='default_blog_detail'),
    path('blog-list.html', RedirectView.as_view(url='/blog/', permanent=True)),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
]
