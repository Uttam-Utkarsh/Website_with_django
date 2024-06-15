from django.shortcuts import render
from myapp.models import Contact
from django.http import HttpResponse  

# Create your views here.

def index(request):
    return render(request,'index.html')

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
    return render(request,'demo.html')