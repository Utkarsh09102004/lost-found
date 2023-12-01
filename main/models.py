from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
# models.py

from django.db import models

class LostItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255,null=True, blank=True)
    date_lost = models.DateField(null=True, blank=True)
    # contact_info = models.CharField(max_length=255)
    image = models.ImageField(upload_to='lost_item_images/', null=True, blank=True)
    loser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name

class FoundItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_found = models.DateField()
    image = models.ImageField(upload_to='found_item_images/', null=True, blank=True)
    founder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
   

    def __str__(self):
        return self.name




class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)


    def __str__(self):
        return self.username