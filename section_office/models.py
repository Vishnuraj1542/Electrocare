from django.db import models

# Create your models here.
class OfficeDetails(models.Model):
    office_name=models.CharField(null=True,blank=True,max_length=50)
    address=models.TextField(null=True,blank=True)
    building_no=models.BigIntegerField(null=True,blank=True)
    district=models.CharField(null=True,blank=True,max_length=80)
    local_body=models.CharField(null=True,blank=True,max_length=70)
    
