"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'webinar$', Webinar.as_view(), name='webinar'),
    url(r'webinar1$', Webinar1.as_view(), name='webinar1'),
    #url(r'course-funnel/(?P<amount>.+)$', CourseFunnel.as_view(), name='course_funnel'),
    url(r'webinarpackage$', WebinarPackage.as_view(), name='webinarpackage'),
    url(r'webinarpackage/(?P<amount>.+)$', WebinarPayoutPackage.as_view(), name='webinar_payout'),
    url(r'signup$', Signup.as_view(), name='signup'),
    url(r'comming-soon$', CommingSoon.as_view(), name='comming-soon'),
    url(r'thank_you$', ThankYou.as_view(), name='thankyou'),
    url(r'coaching$', Coaching.as_view(), name='coaching'),
    url(r'contact$', Contact.as_view(), name='contact'),
    url(r'courses$', Courses.as_view(), name='courses'),
    url(r'testimonials$', Testimonials.as_view(), name='testimonials'),
    url(r'about$', About.as_view(), name='about'),
    url(r'events$', Events.as_view(), name='events'),
    url(r'', Homepage.as_view(), name='index'),
]
