from django.db import models

class employe(models.Model):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=10)
    qualification=models.CharField(max_length=60)
    skills=models.CharField(max_length=100)
    language=models.CharField(max_length=50)
    experience=models.CharField(max_length=10)
    personal_skills=models.CharField(max_length=100)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=10)



class details(models.Model):
    name=models.CharField(max_length=30)
    qualification=models.CharField(max_length=40)
    skills=models.CharField(max_length=100)
    experience=models.CharField(max_length=50)
    personal_skills=models.CharField(max_length=60)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=10)
    company=models.CharField(max_length=30)
