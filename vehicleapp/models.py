from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


class VehicleModel(AbstractUser):
    vehiclename=models.CharField(max_length=100)
    price = models.IntegerField(null=True, blank=True)

    



