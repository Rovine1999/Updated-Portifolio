from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=500, blank=True, null=True)
    message = models.TextField(max_length=5000, blank=True, null=True)
    date_sent = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    category = models.CharField(max_length=100, blank=True, null=True)
    client = models.CharField(max_length=100, blank=True, null=True)
    project_date = models.DateField()
    project_url = models.CharField(max_length=5000, blank=True, null=True)
    project_description = models.TextField(max_length=5000, blank=True, null=True)
    project_image = models.ImageField(upload_to='project_image/')
    date_created = models.DateTimeField(auto_now_add=True)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='project_images/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.client


class Skill(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    percent = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
