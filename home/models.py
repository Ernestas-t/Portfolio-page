from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=200)
    project_url = models.URLField(max_length=200, null=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Experience(models.Model):
    time_frame = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.role


class Education(models.Model):
    time_frame = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    degree_level = models.CharField(max_length=200)
    degree_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.degree_name


class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tech(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
