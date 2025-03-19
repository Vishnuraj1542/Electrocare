from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class LoginDetails(AbstractUser):

    user_type=models.CharField(null=True,blank=True,choices = [('PUBLIC','public'),('ADMIN','admin'),('SECTION OFFICE','section office'),('LINEMAN','lineman')],default='PUBLIC')
    phone=models.CharField(max_length=15,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True)
