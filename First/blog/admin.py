from django.contrib import admin
from blog.models import Contact
from .models import Employee

# admin.site.register(Contact)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Subject','Message')
    list_filter=('Email','Subject')



admin.site.register(Employee)
    
# Register your models here.
