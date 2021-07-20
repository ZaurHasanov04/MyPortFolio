from django.db import models


# Create your models here.


class About(models.Model):
    title=models.TextField(null=False, blank=False)
    inform=models.TextField(null=False, blank=False)
    slogan=models.CharField(max_length=255, null=True)
    fb_link=models.CharField(max_length=180, null=True)
    github_link=models.CharField(max_length=200, null=True)
    linkedin=models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title=models.CharField(max_length=255, null=False, blank=False)
    about=models.TextField(null=False, blank=False)
    link=models.CharField( max_length=280 ,null=False, blank=False)
    
    def __str__(self):
        return self.title


class Skill(models.Model):
    title=models.CharField(max_length=80, null=False, blank=False)
    icons=models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    full_name=models.CharField(max_length=80, null=False, blank=False)
    email=models.EmailField(max_length=100, null=False, blank=False)
    subject=models.CharField(max_length=180, null=False, blank=False)
    text=models.TextField(null=False, blank=False)

    def __str__(self):
        return self.full_name