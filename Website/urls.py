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
from django.contrib.auth import views as auth_views
from . import views as core_views
from forms import LoginForm

urlpatterns = [
    url(r'^login/$', LoginUser.as_view(), name='login'),
    url(r'^signup$', SignupUser.as_view(), name='signup'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'fiftypercentoff', OffPercent.as_view(), name='percentoff'),
    url(r'webinar$', Webinar.as_view(), name='webinar'),
    url(r'webinar1$', Webinar1.as_view(), name='webinar1'),
    url(r'livestreamcourse$', LiveCourses.as_view(), name='livestreamcourse'),
    url(r'easterspecial', EasterSpecial.as_view(), name='easterspecial'),
    #url(r'course-funnel/(?P<amount>.+)$', CourseFunnel.as_view(), name='course_funnel'),
    #url(r'webinarpackage$', WebinarPackage.as_view(), name='webinarpackage'),
    url(r'3easypayments', EasyPayments.as_view(), name='3easypayments'),
    url(r'webinarpackage/(?P<amount>.+)$', WebinarPayoutPackage.as_view(), name='webinar_payout'),
    url(r'signup$', Signup.as_view(), name='signup'),
    url(r'comming-soon$', CommingSoon.as_view(), name='comming-soon'),
    url(r'thank_you$', ThankYou.as_view(), name='thankyou'),
    url(r'coaching$', Coaching.as_view(), name='coaching'),
    url(r'contact$', Contact.as_view(), name='contact'),
    url(r'courses$', Courses.as_view(), name='courses'),
    url(r'testimonials$', Testimonials.as_view(), name='testimonials'),
    url(r'about$', About.as_view(), name='about'),
    url(r'^createevents$', CreateEve.as_view(), name='createeve'),
    url(r'^events$', Events.as_view(), name='events'),
    url(r'^fixnflips$', FixnFlips.as_view(), name='fixnflips'),
    url(r'^wholesalingcontractnassignment$', WholeSale.as_view(), name='wholesalingcontractnassignment'),
    url(r'^subjecttoexistingfinance$', ExistingFinance.as_view(), name='subjecttoexistingfinance'),
    url(r'^completeshortsaleprocess$', ShortSale.as_view(), name='completeshortsaleprocess'),
    url(r'^brozepackage$', BronzePackage.as_view(), name='brozepackage'),
    url(r'^silverpackage$', SilverPackage.as_view(), name='silverpackage'),
    url(r'^goldpackage$', GoldPackage.as_view(), name='goldpackage'),
    url(r'', Homepage.as_view(), name='index'),


]
