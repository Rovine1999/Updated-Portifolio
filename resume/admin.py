from django.contrib import admin
from .models import *
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['category', 'client', 'project_date', 'project_url', 'project_description']


class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'percent', 'position']


admin.site.register(Message, MessageAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Skill, SkillAdmin)
