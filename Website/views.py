from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.mail import send_mail
from Website.settings import EMAIL_HOST
from Website.settings import CLIENT_ID, LIVE_CLIENT_ID
from Website.models import Users
from Website.forms import LoginForm
from Website.models import *
from Website.models import Events as EventsModel
import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import PBKDF2PasswordHasher


class SignupUser(View):
    def get(self, request):
        if not request.session.get('logged_in', None):
            return render(request, 'registration/signup.html')
        else:
            # return render(request, 'index.html')
            return redirect('/')


    def post(self , request):
        data= request.POST
        hasher=PBKDF2PasswordHasher()
        name=data['name']
        email=data['email']
        password=data['password']
        password2=data['c_password']
        date_joined=datetime.datetime.now()
        message=''
        if(password == password2):
            password=hasher.encode(password=password,salt='salt',iterations=50000)
            try:
                # events_data=EventsForm.objects.get(event_date=date)
                Front_Users.objects.get(email=email)
                return render(request, 'registration/signup.html',{'message':'Email Already exists '})                
            except Front_Users.DoesNotExist: 
                events= Front_Users(name=name,email=email,password=password,date_joined=date_joined)
                events.save()
                
                request.session['logged_in']=True
                request.session['username']=email
                request.session['name']=name
                print('You signed up successfully')
                return redirect('/thank_you')
        else:
            return render(request, 'registration/signup.html',{'message':'Passwords do not match'})

class Logout(View):
    def get(self,request):
        if request.session.get('logged_in', None):
            del request.session['logged_in']
            del request.session['username']
            del request.session['name']
            # return render(request, 'registration/login.html')
            return redirect('/login/')
        else:
            return redirect('/')




class LoginUser(View):
    def get(self, request):
        data=Front_Users.objects.all()
        if not request.session.get('logged_in', None):
            return render(request, 'registration/login.html',{'data':data})
        else:
            # return render(request, 'index.html',{'data':data})
            return redirect('/')


    # def post(self , request):
    #     data= request.POST
    #     hasher=PBKDF2PasswordHasher()
    #     email=data['email']
    #     password=data['password']
    #     message=''
    #     password=hasher.encode(password=password,salt='salt',iterations=50000)
    #     try:
    #         # events_data=EventsForm.objects.get(event_date=date)

    #         user_data=Front_Users.objects.get(email=email,password=password)

    #         request.session['name']=user_data.name
    #         request.session['logged_in']=True
    #         request.session['username']=user_data.email
    #         return render(request, 'profile.html')
    #     except Front_Users.DoesNotExist: 
    #         # events= EventsForm(title=title,description=description)
    #         # print('user not logged in')          
    #         return render(request, 'registration/login.html',{'message':'Email Does not exists '})
# 
    def post(self , request):
        data= request.POST
        hasher=PBKDF2PasswordHasher()
        email=data['email']
        password=data['password']
        message=''
        password=hasher.encode(password=password,salt='salt',iterations=50000)
        try:
            # events_data=EventsForm.objects.get(event_date=date)

            Front_Users.objects.get(email=email)
            try:
                user_data=Front_Users.objects.get(password=password)
                request.session['name']=user_data.name
                request.session['logged_in']=True
                request.session['username']=user_data.email
                return render(request, 'profile.html')

            except Front_Users.DoesNotExist:
                return render(request,'registration/login.html',{'message':'Password entered is Incorrect'})

        except Front_Users.DoesNotExist: 
            # events= EventsForm(title=title,description=description)
            # print('user not logged in')
            
            return render(request,'registration/login.html',{'message':'Email Does not exists ','email':email})

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
        formatedDate = today.strftime("%Y-%m-%d")
        form_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        # print(today)
        print(formatedDate)
        print(form_date)
        check = False
        saved = False
        if form_date < today:
            check = False
        else:
            print('test')
            try:
                # events_data=EventsForm.objects.get(event_date=date)
                Events.objects.get(event_date=date)
            except Events.DoesNotExist: 
                # events= EventsForm(title=title,description=description)
                events= Events(title=title,description=description,event_date=date)
                events.save()
                saved= True
        # events.title=title
        # events.description=description
        return render(request,'createevents.html',{'saved':saved,'today':today,'date':date,'check':check})

class Event_access(View):
    def get(self,request,title):
        print(title);

    def post(self,request):
        data=request.POST
        print(data.title)




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
        data=EventsModel.objects.all()
        # print(data)
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
            'live_id': LIVE_CLIENT_ID,
            
        }
        return render(request,'goldpackage.html',data)

class OffPercent(View):
    def get(self,request):
        data = {
            'client_id': CLIENT_ID,
            'currency': 'USD',
            'live_id': LIVE_CLIENT_ID
            
        }
        return render(request,'50percentOff.html', data)


class Profile(View):
    def get(self,request):
        if not request.session.get('logged_in', None):
            return redirect('index')
        else:
            return render(request,'profile.html')

class Blogs(View):
    def get(self,request):
        
        return render(request,'blogs.html')
        

class Update_name(View):
    def get(self,request):
        return redirect('/profile')


    def post(self,request):
        data=request.POST
        updatename=data['name']
        # email=data['email']
        currentemail=request.session['username']
        #print(name)
        #print(email)
      
                # events_data=EventsForm.objects.get(event_date=date)
        try:
            obj=Front_Users.objects.get(email=currentemail)
            obj.name = updatename
            #print(obj.name)
            obj.save()
            request.session['name']=updatename
            return render(request, 'profile.html',{'message':'Details Updated'})
        except Front_Users.DoesNotExist:
            print('test')
            return render(request, 'profile.html',{'message':'Passwords do not match'})

class Update_pass(View):
    def get(self,request):
        return redirect('/profile')
    def post(self,request):
        data=request.POST
        oldpass=data['oldpass']
        newpass=data['newpass']
        conpass=data['conpass']
        currentemail=request.session['username']
        hasher=PBKDF2PasswordHasher()
        obj=Front_Users.objects.get(email=currentemail)
        dbpass= obj.password
        print(dbpass)
        oldpass=hasher.encode(password=oldpass,salt='salt',iterations=50000)
        print(oldpass)
        if oldpass==dbpass:
            if newpass == conpass:
                
                try:
                    obj=Front_Users.objects.get(email=currentemail)
                    newpass=hasher.encode(password=newpass,salt='salt',iterations=50000)
                    obj.password = newpass
                    obj.save()
                    return render(request, 'profile.html',{'message':'Password Updated'})
                except Front_Users.DoesNotExist:
                    return render(request, 'profile.html',{'message':'Something went wrong, please try again'})                   


            else:
                return render(request, 'profile.html',{'message':'Confirm Password is not the same'})
        else:
            return render(request, 'profile.html',{'message':'Old Password Entered Incorrectly'})
        #print(checkpass)
        #print(oldpass)
        # print(newpass)
        # print(conpass)
        
        return redirect('/profile')

   

