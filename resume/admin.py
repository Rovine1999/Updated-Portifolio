from django.contrib import admin
from .models import *
# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['category', 'client', 'project_date', 'project_url', 'project_description']


class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'percent', 'position']

class EducationAdmin(admin.ModelAdmin):
    list_display = ['school', 'qualification', 'start_date', 'end_date']

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'start_date', 'end_date']

# class ReferenceAdmin(admin.ModelAdmin):
#     list_display = ['name', 'company', 'position', 'phone', 'email']

# class LanguageAdmin(admin.ModelAdmin):
#     list_display = ['name', 'level']

# class InterestAdmin(admin.ModelAdmin):
#     list_display = ['name']

# class AwardAdmin(admin.ModelAdmin):
#     list_display = ['name', 'date', 'description']

# class CertificationAdmin(admin.ModelAdmin):
#     list_display = ['name', 'date', 'description']


admin.site.register(Message, MessageAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)

#run python manage.py makemigrations