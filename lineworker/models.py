from django.db import models
from section_office.models import OfficeDetails

# Create your models here.
class WorkerDetails(models.Model):
    name=models.CharField(null=True,blank=True,max_length=30)
    address=models.TextField(null=True,blank=True)
    worker_id=models.BigIntegerField(null=True,blank=True)
    section_Office=models.ForeignKey(OfficeDetails,null=True,blank=True,on_delete=models.CASCADE)
