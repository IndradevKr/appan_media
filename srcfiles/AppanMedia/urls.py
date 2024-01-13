from django.urls import path
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("services", views.services, name="services"), 
    path("thanks/", views.thanks, name="thanks"),
    path("blogs/", views.blogs, name="blogs"),
    path("view-blog/<slug>", views.view_blogs, name="view_blog" ),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)