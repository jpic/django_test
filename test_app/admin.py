from django.contrib import admin

import autocomplete_light

from models import *


class ProjectAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(Project)
admin.site.register(Project, ProjectAdmin)


class MemberAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(Member)
admin.site.register(Member, MemberAdmin)
