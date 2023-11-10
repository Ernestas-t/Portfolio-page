from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('update-experience/', views.updateExperience, name='update-experience'),
    path('update-education/', views.updateEducation, name='update-education'),
    path('update-project/', views.updateProject, name='update-project'),
    path('add-item/', views.addItem, name='add-item'),
]