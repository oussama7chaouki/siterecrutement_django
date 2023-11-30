from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    avatar = models.ImageField(null=True, default="avatar-01.jpg")
    role = models.IntegerField(default=1)
    status = models.IntegerField(default=1)
    activation = models.IntegerField(default=1)

    REQUIRED_FIELDS = []

class Job(models.Model):
    id_job = models.AutoField(primary_key=True)
    recruter = models.ForeignKey(User, on_delete=models.CASCADE)
    domain = models.CharField(max_length=55)
    company = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()
    job_salaire = models.IntegerField()
    date = models.DateField()
    formationreq = models.CharField(max_length=100)
    expreq = models.IntegerField()
    skillreq = models.CharField(max_length=255)
class Candidature(models.Model):
    id_candidature = models.AutoField(primary_key=True)
    candidat = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date = models.DateField()
    score = models.IntegerField(default=0)
    reqexp = models.CharField(max_length=50)
    reqfor = models.CharField(max_length=50)
    reqskill = models.IntegerField()
    status = models.CharField(max_length=100, default='Waiting')


