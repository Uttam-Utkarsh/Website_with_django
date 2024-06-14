from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def admission(request):
    return render(request,'admissionForm.html')

def contactus (request):
    return render(request,'contactUS.html')

def gallery(request):
    return render(request,'gallery.html')

def news(request):
    return render(request,'news.html')

def demo(request):
    return render(request,'demo.html')