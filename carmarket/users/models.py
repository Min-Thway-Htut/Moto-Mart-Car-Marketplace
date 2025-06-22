from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CarBrandNames(models.Model):
    car_brand_names = models.TextField()

    def __str__(self):
        return self.car_brand_names
    