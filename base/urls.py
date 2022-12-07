from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('blogs/', blogs_list, name='blogs_list'),
    path('guestblogs/', guest_blogs_list, name='guest_blog_list'),
    path('aboutblogs/', about_blog, name='about_blog'),
    path('aboutme/', about_me, name='about_me'),
    path('blogs/<int:id>/', blog_view, name='blog_view'),
    path('subscriber/', subscriber_page, name='subscriber_page')
]
