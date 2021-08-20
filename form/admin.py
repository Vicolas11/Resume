from form.models import ContactModel
from django.contrib import admin

# @admin.register(BlogPost)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','subject','message',)
    list_display_links = ('id','email',)
    search_fields = ('email','subject',)
    ordering = ('id',)

admin.site.register(ContactModel, ContactModelAdmin)