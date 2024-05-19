from django.db import models

class organization(models.Model):
    com_name=models.CharField(max_length=60)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    post=models.CharField(max_length=30)
    skills=models.CharField(max_length=60)
    language=models.CharField(max_length=60)
    experience=models.CharField(max_length=100)
    qualification=models.CharField(max_length=50)
    about=models.TextField()

class emp_detail(models.Model):
    name=models.CharField(max_length=30)
    post=models.CharField(max_length=30)
    profile=models.CharField(max_length=40)
    company=models.CharField(max_length=30)


