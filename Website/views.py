from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.mail import send_mail
from Website.settings import EMAIL_HOST
from Website.settings import CLIENT_ID, LIVE_CLIENT_ID
from Website.models import Users
from Website.forms import LoginForm
from Website.models import EventsForm
import datetime

class CreateEve(View):
    def get(self, request): 
        data=EventsForm.objects.all()
        today = datetime.datetime.today()
        return render(request, 'createevents.html',{'data':data,'today':today})

    def post(self, request):
        data= request.POST
        saved= 'FALSE'
        title=data['title']
        description = data['description']
        date=data['date'];
        today = datetime.datetime.today()
        check = False
        saved = False
        try:
            # events_data=EventsForm.objects.get(event_date=date)
            EventsForm.objects.get(event_date=date)
        except EventsForm.DoesNotExist: 
            # events= EventsForm(title=title,description=description)
            events= EventsForm(title=title,description=description,event_date=date)
            events.save()
            saved= True
        # events.title=title
        # events.description=description
        return render(request,'createevents.html',{'saved':saved,'today':today,'date':date,'check':check})

class Homepage(View):
    def get(self, request):
        return render(request, 'index.html')


class Coaching(View):
    def get(self, request):
        return render(request, 'coaching.html')

class LiveCourses(View):
    def get(self, request):
        data = {
            'amount': 19.97,
            'client_id': CLIENT_ID,
            'currency': 'USD',
            'live_id': LIVE_CLIENT_ID
        }
        return render(request, 'livestreamcourses.html', data)

class CommingSoon(View):
    def get(self, request):
        return render(request, 'comming-soon.html')

class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        data = request.POST
        email = data['email']
        name = data['name']
        message = data['message'] + '\n\n email:' + email + '   \n\n\nname: ' + name
        send_mail(subject='Contact Us', message=message, from_email=EMAIL_HOST, recipient_list=['valdoconsultingllc@gmail.com'])
        return render(request, 'thank-you.html')




class WebinarPackage(View):
    def get(self, request):
        data = {
            'amount': 997,
            'client_id': CLIENT_ID,
            'currency': 'USD',
            'live_id': LIVE_CLIENT_ID
        }
        return render(request, 'webinarpackage.html', data)


class EasyPayments(View):
    def get(self, request):
        data = {
            'amount': 333,
            'client_id': CLIENT_ID,
            'currency': 'USD',
            'live_id': LIVE_CLIENT_ID
        }
        return render(request, '3easypayments.html', data)

class EasterSpecial(View):
    def get(self, request):
        data = {
            'amount': 97,
            'client_id': CLIENT_ID,
            'currency': 'USD',
            'live_id': LIVE_CLIENT_ID
        }
        return render(request, 'easterspecial.html', data)

class WebinarPayoutPackage(View):
    def get(self, request, amount):
        try:
            amount = float(amount)
        except:
            return render(request, 'index.html')
        data = {
            'amount': amount,
            'client_id': CLIENT_ID,
            'currency': 'USD',
            'live_id': LIVE_CLIENT_ID
        }
        return render(request, 'webinarpackage.html', data)

class Courses(View):
    def get(self, request):
        return render(request, 'courses1.html')



class Events(View):
    def get(self, request):
        data=EventsForm.objects.all()
        return render(request, 'events.html',{'data':data})


class Testimonials(View):
    def get(self, request):
        return render(request, 'testmonials.html')


class About(View):
    def get(self, request):
        return render(request, 'about.html')


class ThankYou(View):
    def get(self, request):
        return render(request, 'thank-you.html')


class Webinar(View):
    def get(self, request):
        return render(request, 'webinar.html')


class Webinar1(View):
    def get(self, request):
        return render(request, 'webinar1.html')


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        checkbox = request.POST.get('brand1')
        if password == c_password:
            user = Users(username=name, email=email)
            user.set_password(password)
            user.save()
            return redirect('index')

        return render(request, 'signup.html', {'error': "Errors in Form."})


class CourseFunnel(View):
    def get(self, request, amount):
        amount = float(amount)
        data = {
            'amount': amount,
            'client_id': CLIENT_ID,
            'currency': 'USD'
        }
        return render(request, 'course-funnel.html', data)


class FixnFlips(View):
    def get(self, request):
        return render(request, 'fixnflips.html')

class WholeSale(View):
    def get(self, request):
        return render(request, 'wholesalingcontractnassignment.html')

class ExistingFinance(View):
    def get(self, request):
        return render(request, 'subjecttoexistingfinance.html')

class ExistingFinance(View):
    def get(self, request):
        return render(request, 'subjecttoexistingfinance.html')

class ShortSale(View):
    def get(self, request):
        return render(request, 'completeshortsaleprocess.html')

class BronzePackage(View):
    def get(self,request):
        data = {
            'client_id': CLIENT_ID,
            'currency': 'USD',
            'live_id': LIVE_CLIENT_ID
        }
        return render(request, 'bronzepackage.html',data)

class SilverPackage(View):
    def get(self,request):
        data = {
            'client_id': CLIENT_ID,
            'currency': 'USD',
            'live_id': LIVE_CLIENT_ID
        }
        return render(request ,'silverpackage.html',data)

class GoldPackage(View):
    def get(self,request):
        data = {
            'client_id': CLIENT_ID,
            'currency': 'USD',
            'live_id': LIVE_CLIENT_ID
        }
        return render(request,'goldpackage.html',data)





  
