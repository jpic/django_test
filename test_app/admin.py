from django.contrib import admin

from models import *


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('message', 'email')
admin.site.register(Complaint, ComplaintAdmin)


class ResponseLetterAdmin(admin.ModelAdmin):
    list_display = ('date_response', 'response_from', 'complaint')
admin.site.register(ResponseLetter)
