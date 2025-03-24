from django.db import models
from log_manager.models import LoginDetails
from section_office.models import OfficeDetails

class PublicDetails(models.Model):
    name=models.CharField(max_length=40,null=True,blank=True)
    dp=models.ImageField(null=True,blank=True,upload_to='profile')
    city=models.CharField(max_length=20,null=True,blank=True)
    house_no=models.CharField(null=True,blank=True,max_length=10)
    address=models.TextField(null=True,blank=True)
    consumer_id=models.IntegerField(null=True,blank=True)
    sectionoffice=models.OneToOneField(OfficeDetails,on_delete=models.CASCADE,null=True,blank=True)
    user_details=models.OneToOneField(LoginDetails,on_delete=models.CASCADE,null=True,blank=True)

