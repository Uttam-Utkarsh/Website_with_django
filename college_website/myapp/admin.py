from django.contrib import admin 
from myapp.models import Contact,Profile,Registration_form,Notice,Programs,Testimonials,StudentResult,StudentNotification

# Register your models here.

admin.site.site_header = 'College Admin Panel'

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Email','Description', 'added_on', 'is_active']
    
    
# class Registration_form(admin.ModelAdmin):
#     list_display = ['id','student_first_name','student_last_name',]

admin.site.register(Contact, ContactAdmin)
admin.site.register(Profile)
admin.site.register(Registration_form)
admin.site.register(Notice)
admin.site.register(Programs)
admin.site.register(Testimonials)
admin.site.register(StudentNotification)
admin.site.register(StudentResult)

