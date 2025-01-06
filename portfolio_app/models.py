from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Add a picture
    brief_description = models.TextField(blank=True, null=True)  # Add a brief description

    def __str__(self):
        return self.name

class Education(models.Model):
    Institue = models.CharField(max_length=100)
    Degree = models.CharField(max_length=100)
    Start_year = models.DateField(blank=True, null=True)
    Graduation_year = models.DateField(blank=True, null=True)
    Picture = models.ImageField(upload_to='imgs/', blank=True, null=True)  # Add a picture

    def __str__(self):
        return self.Institue

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issued_by = models.CharField(max_length=100)
    issue_date = models.DateField()
    certificate_link = models.URLField(blank=True, null=True)
    Picture = models.ImageField(upload_to='imgs/', blank=True, null=True)  # Add a picture


    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    tech_stack = models.CharField(max_length=200)
    project_link = models.URLField(blank=True, null=True)
    Picture = models.ImageField(upload_to='imgs/', blank=True, null=True)  # Add a picture


    def __str__(self):
        return self.title

class Contact(models.Model):
    GitHub = models.URLField(blank=True, null=True)
    LinkedIn = models.URLField(blank=True, null=True)
    Whatsapp = models.URLField(blank=True, null=True)
    PHONE = models.IntegerField(blank=True, null=True)
    Email = models.EmailField()
    CV = models.FileField(upload_to='files/', blank=True, null=True)


    def __str__(self):
        return f"Contact information for {Profile.name}"
