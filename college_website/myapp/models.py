from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Description = models.TextField(default="Nothings Happens")
    added_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.Name
    
    class Meta:
        verbose_name =  "Contact Table"
        
        
        
class Profile(models.Model):
    P_Name = models.CharField(max_length=100,default='none')
    P_Email = models.CharField(max_length=100,default='none')
    P_Password = models.CharField(max_length=100,default='none')
    P_Rollno = models.CharField(max_length=10,default='none')
    P_Subject = models.CharField(max_length=20,default='none')
    P_PhoneNo = models.CharField(max_length=20,default='none')
    P_Blood_group = models.CharField(max_length=10,default='none')
    P_Image = models.ImageField(upload_to="Profile_image/")
    def __str__(self):
        return self.P_Name + ' - ' + self.P_Email
    
    class Meta:
        verbose_name =  "Profile Table"
        

class Registration_form(models.Model):
    student_first_name = models.CharField(max_length=10)
    student_last_name = models.CharField(max_length=10)
    student_date_of_birth = models.DateField(blank=True)
    student_email = models.EmailField(max_length=30)
    student_phonenumber = models.CharField(max_length=15)
    student_gender = models.CharField(max_length=10)
    student_address = models.CharField(max_length=100)
    student_city = models.CharField(max_length=10)
    student_pincode = models.CharField(max_length=6)
    student_state = models.CharField(max_length=10)
    student_country = models.CharField(max_length=10)
    student_hobbies = models.CharField(max_length=10)
    student_course = models.CharField(max_length=10)
    student_class10_board = models.CharField(max_length=20,default='Null')        
    student_class10_perc = models.CharField(max_length=20,default='Null')        
    student_class10_year_of_pass = models.CharField(max_length=20,default='Null')        
    student_class12_board = models.CharField(max_length=20,default='Null')        
    student_class12_perc = models.CharField(max_length=20,default='Null')        
    student_class12_year_of_pass = models.CharField(max_length=20,default='Null')        
    student_graduation_board = models.CharField(max_length=20,default='Null')        
    student_graduation_perc = models.CharField(max_length=20,default='Null')        
    student_graduation_year_of_pass = models.CharField(max_length=20,default='Null')        
    student_masters_board = models.CharField(max_length=20,default='Null')        
    student_masters_perc = models.CharField(max_length=20,default='Null')        
    student_masters_year_of_pass = models.CharField(max_length=20,default='Null') 
    
    def __str__(self):
        return self.student_first_name + ' ' + self.student_last_name
    
    class Meta:
        verbose_name =  "Students Data"   
        
# for news and event section

category = (
    ("Events","Events"),
    ("Campus-News","Campus News"),
    ("Notice","Notice")
)

class Notice(models.Model):
    category = models.CharField(max_length=20,choices= category,default="Events")
    description = models.TextField(max_length=200) 
    
    def __str__(self):
        return self.category + " : " + self.description
    
    
# Academic programes

category = (
    ("Bachelor","Bachelor"),
    ("Master","Master"),
    ("Phd","Phd")
)

class Programs(models.Model):
    category = models.CharField(max_length=20,choices=category,default="Bachelor")
    title = models.TextField(max_length=20)
    
    def __str__(self):
        return self.category + " : " + self.title
    
    
    
# for testmonials

class Testimonials(models.Model):
    name = models.CharField(max_length=20,default='')
    feedback = models.TextField(max_length=200)
    given_star = models.IntegerField(default=1)
    stars = models.IntegerField(default=0)
    pic = models.ImageField(upload_to="Profile_image/",default='')
    
    def __str__(self):
        return self.name + ' - ' + self.feedback
    
    
    

    