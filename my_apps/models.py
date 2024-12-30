from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    url = models.URLField()
    github_repo = models.URLField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.name
