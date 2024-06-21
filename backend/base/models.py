from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.

ROLE_CHOICES = [
  ('admin', 'Admin'),
  ('editor', 'Editor'), 
  ('viewer', 'Viewer')
]

TYPE_WORK = [
  ('presencial', 'Presencial'),
  ('hybrid', 'Hybrid'), 
  ('remote', 'Remote')
]

class Company(models.Model):
    name = models.CharField(max_length=50)
    ubication = models.TextField()
    description = models.TextField()
    
class Skill(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

class Project(models.Model):
    name = models.CharField(max_length=100)
    company_id = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE, related_name="projects")
    personal = models.BooleanField()
    skills_ids = models.ManyToManyField(Skill)

class WorkExperience(models.Model):
    company_id = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE, related_name="work_experiences")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    type = models.CharField(
        max_length=10,
        choices= TYPE_WORK,
        null=True
    )
    charge = models.CharField(max_length=80)

class Course(models.Model):
    name = models.CharField(max_length=80)
    skills_ids = models.ManyToManyField(Skill)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)