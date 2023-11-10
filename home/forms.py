from django.forms import ModelForm
from .models import Experience, Education, Project, Skill, Tech

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

class TechForm(ModelForm):
    class Meta:
        model = Tech
        fields = '__all__'