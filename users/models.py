from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(default='1900-01-01')
    address1 = models.CharField(max_length=100, default=' ')
    address2 = models.CharField(max_length=100, default=' ')
    city = models.CharField(max_length=50, default=' ')
    state = models.CharField(max_length=25, default=' ')
    zip = models.CharField(max_length=5, default=' ')
    phone = models.CharField(max_length=25, default=' ')
    type = models.CharField(max_length=25, default=' ')