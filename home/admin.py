from django.contrib import admin
from .models import Project, Education, Experience, Skill, Tech

# Register your models here.
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Tech)