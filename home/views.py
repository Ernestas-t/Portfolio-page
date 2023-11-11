from django.shortcuts import render, redirect
from .models import Project, Experience, Education, Skill, Tech
from .forms import ExperienceForm, EducationForm, ProjectForm, SkillForm, TechForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
    return render(request, 'home/index.html')


def resume(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    techs = Tech.objects.all()

    context = {'experiences': experiences, 'educations': educations, 'skills': skills, 'techs': techs}
    return render(request, 'home/resume.html', context)


def projects(request):
    projects = Project.objects.all()

    context = {'projects': projects}
    return render(request, 'home/projects.html', context)


def contact(request):
    return render(request, 'home/contact.html')


@login_required()
def updateExperience(request):
    form = ExperienceForm()
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume')
    context = {'form': form}
    return render(request, 'home/update_experience.html', context)


@login_required()
def updateEducation(request):
    form = EducationForm()
    if request.method == 'POST':
        print('test')
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume')
    context = {'form': form}
    return render(request, 'home/update_education.html', context)


@login_required()
def updateProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        print('test')
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'home/update_project.html', context)


@login_required()
def addItem(request):
    if request.GET.get('q') == 'language':
        form = TechForm()
        if request.method == 'POST':
            form = TechForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form': form, 'text': 'Library / Framework'}
    else:
        form = SkillForm()
        if request.method == 'POST':
            form = SkillForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('resume')
        context = {'form': form, 'text': 'Professional Skill'}
    return render(request, 'home/add_item.html', context)

@login_required()
def deleteData(request, pk):
    if request.GET.get('data') == 'experience':
        experience = Experience.objects.get(id=pk)
        if request.method == 'POST':
            experience.delete()
            return redirect('resume')
        context = {'data': experience.role}
    elif request.GET.get('data') == 'education':
        education = Education.objects.get(id=pk)
        if request.method == 'POST':
            education.delete()
            return redirect('resume')
        context = {'data': education.degree_name}
    elif request.GET.get('data') == 'skill':
        skill = Skill.objects.get(id=pk)
        if request.method == 'POST':
            skill.delete()
            return redirect('resume')
        context = {'data': skill.name}
    elif request.GET.get('data') == 'tech':
        tech = Tech.objects.get(id=pk)
        if request.method == 'POST':
            tech.delete()
            return redirect('resume')
        context = {'data': tech.name}
    elif request.GET.get('data') == 'project':
        project = Project.objects.get(id=pk)
        if request.method == 'POST':
            project.delete()
            return redirect('projects')
        context = {'data': project.name}
    return render(request, 'home/delete_data.html', context)