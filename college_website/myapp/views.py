from django.shortcuts import render
from myapp.models import Contact,Profile,Registration_form,Notice,Programs
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login, logout 
import datetime
import time

# Create your views here.

def index(request):
    
    academic_data = Programs.objects.all()
    context={
        'academic_data':academic_data,
    }
    if request.method == 'POST':
        Name = request.POST.get('U_name')
        Email = request.POST.get('U_email')
        Password = request.POST.get('U_password')
        obj = User.objects.create_user(Email, Email, Password)
        obj.save()
        pro = Profile(P_Name = Name, P_Email = Email, P_Password = Password)
        pro.save()
        context['status']= (f'Dear {Name} you are Registered Successfully')
    
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'aboutus.html')

def admission(request):
    
    context={}
    if request.method == 'POST':
        FName = request.POST.get('firstusername')
        LName = request.POST.get('lastusername')
        # DOB = request.POST.get('Year')+ '-' + request.POST.get('month') +'-' + request.POST.get('day')
        DOB = datetime.date(int(request.POST.get('Year')), int(request.POST.get('month')), int(request.POST.get('day')))
        Email = request.POST.get('email')
        PNo = request.POST.get('number')
        Gender = request.POST.get('gender')
        Address = request.POST.get('address')
        City = request.POST.get('city')
        Pin = request.POST.get('pin')
        State = request.POST.get('state')
        Country = request.POST.get('country')
        Hobbies = request.POST.get('HOBBIES')
        cl_x_board = request.POST.get('cl_x_board')
        cl_x_Per = request.POST.get('cl_x_Per')
        cl_x_year = request.POST.get('cl_x_year')
        cl_12_board = request.POST.get('cl_12_board')
        cl_12_Per = request.POST.get('cl_12_Per')
        cl_12_year = request.POST.get('cl_12_year')
        cl_g_board = request.POST.get('cl_g_board')
        cl_g_Per = request.POST.get('cl_g_Per')
        cl_g_year = request.POST.get('cl_g_year')
        cl_m_board = request.POST.get('cl_m_board')
        cl_m_Per = request.POST.get('cl_m_Per')
        cl_m_year = request.POST.get('cl_m_year')
        Course = request.POST.get('COURSES')
        obj = Registration_form(student_first_name = FName, student_last_name = LName, student_date_of_birth = DOB, student_email = Email, student_phonenumber = PNo, student_gender = Gender, student_address = Address, student_city = City, student_pincode = Pin, student_state = State, student_country = Country, student_hobbies = Hobbies, student_course = Course, student_class10_board = cl_x_board, student_class10_perc = cl_x_Per, student_class10_year_of_pass = cl_x_year, student_class12_board = cl_12_board, student_class12_perc = cl_12_Per, student_class12_year_of_pass = cl_12_year, student_graduation_board = cl_g_board, student_graduation_perc = cl_g_Per, student_graduation_year_of_pass = cl_g_year, student_masters_board = cl_m_board, student_masters_perc = cl_m_Per, student_masters_year_of_pass = cl_m_year )
        obj.save()
        context['mesg']= (f'Dear {FName} Registered Succesfull')
        # time.sleep(2)
        # return HttpResponseRedirect('/')
    return render(request,'admissionForm.html',context)

def contactus (request):
    context={}
    if request.method == 'POST':
        Name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        message = request.POST.get('user_description')
        obj = Contact(Name = Name, Email = email, Description = message)
        obj.save()
        context['message2']= (f'Dear {Name} Thanks for contacting us')
    return render(request,'contactUS.html',context)

def gallery(request):
    return render(request,'gallery.html')

def news(request):
    all_data = Notice.objects.all().values()
    context={
        'all_data':all_data,
    }
    return render(request,'news.html',context)

def login(request):
    context={}
    if request.method == 'POST':
        user_email = request.POST.get('emailaddress')
        user_password = request.POST.get('userpassword')
        check_user = authenticate(username=user_email, password=user_password)
        if check_user:
            login(request)
            context['name']= user_email
            return render(request,'login.html',context)
        else:
            context['status']= 'Invalid Credentials'
            return render(request,'index.html',context) 

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def faculty(request):
    return render(request,'faculty.html')