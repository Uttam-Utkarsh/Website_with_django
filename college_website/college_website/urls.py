"""
URL configuration for college_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls,name=admin),
    path('',views.index, name='index'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('contactus/',views.contactus, name='contactus'),
    path('gallery/',views.gallery, name='gallery'),
    path('news/',views.news, name='news'),
    path('admission/',views.admission, name='admission'),
    path('myaccount/',views.myaccount, name='myaccount'),
    path('mylogin/',views.mylogin, name='mylogin'),
    path('user_logout/',views.user_logout, name='user_logout'),
    path('faculty/',views.faculty, name='faculty'),
    path('updateprofile/',views.updateprofile, name='updateprofile'),
    path('feedbackform/',views.feedbackform, name='feedbackform'),
    path('showResult/',views.showResult, name='ShowResult'),
    path('showNotice/',views.showNotice, name='ShowNotice'),
]
if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
