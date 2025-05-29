from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class LoginDetails(AbstractUser):
    user_type=models.CharField(max_length=20,null=True,blank=True,choices=[('Admin','admin'),('Public','public'),('Office','office'),('Worker','worker')],default='Public')
    phone=models.CharField(max_length=19,null=True,blank=True)
    is_active=models.BooleanField(default=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username

