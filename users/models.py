from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255,default='')
    email = models.CharField(max_length=255,unique=True)
    password =models.CharField(max_length=255)
    username =None
    created_date = models.DateTimeField('Date created', default=timezone.now)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    