from django.contrib import admin
from .models import Profile, Project, Skill, Certificate, Contact, Education

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'brief_description')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Certificate)
admin.site.register(Project)
admin.site.register(Contact)
