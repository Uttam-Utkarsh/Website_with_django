from django.contrib import admin 
from myapp.models import Contact,Profile,Registration_form

# Register your models here.

admin.site.site_header = ' Indian College Admin'

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Email','Description', 'added_on', 'is_active']
    
    
# class Registration_form(admin.ModelAdmin):
#     list_display = ['id','student_first_name','student_last_name',]

admin.site.register(Contact, ContactAdmin)
admin.site.register(Profile)
admin.site.register(Registration_form)

