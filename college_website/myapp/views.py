from django.shortcuts import render
from myapp.models import Contact,Profile
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login, logout 

# Create your views here.

def index(request):
    context={}
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
    return render(request,'admissionForm.html')

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
    return render(request,'news.html')

def demo(request):
    context={}
    if request.method == 'POST':
        user_email = request.POST.get('emailaddress')
        user_password = request.POST.get('userpassword')
        check_user = authenticate(username=user_email, password=user_password)
        if check_user:
            login(request,check_user)
            # return HttpResponseRedirect('/demo')
            context['name']= user_email
        else:
            context['status']= 'Invalid Credentials'
            return render(request,'index.html',context) 
    return render(request,'demo.html',context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')