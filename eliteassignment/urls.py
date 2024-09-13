"""
URL configuration for eliteassignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path

from eliteassignment.settings import DEBUG
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('blog', views.blog, name='blog'),
    path('detail', views.detail, name='detail'),
    path('price', views.price, name='price'),
    path('feature', views.feature, name='feature'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('quote', views.quote, name='quote'),
    path('contact', views.contact, name='contact'),

]

if DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

else:
    urlpatterns += [ path(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_ROOT }),
                     # url(r'^uploads/course_photo/(?P<file>.*)$', views.serve_protected_document,
                     #     name='serve_protected_document'),

                     path(r'^uploads/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]
