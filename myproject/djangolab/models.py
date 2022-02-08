from django.db import models

# Create your models here.

class Myusers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    intake_id = models.ForeignKey('Intake', on_delete=models.CASCADE)

class Intake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)



