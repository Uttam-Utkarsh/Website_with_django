from django.contrib import admin
from myapp.models import Contact 

# Register your models here.

admin.site.site_header = ' Indian College Admin'

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Email','Description', 'added_on', 'is_active']

admin.site.register(Contact, ContactAdmin)

