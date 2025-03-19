from django.db import models

# Create your models here.
class WorkerDetails(models.Model):
    name=models.CharField(null=True,blank=True,max_length=30)
    dob=models.DateField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
