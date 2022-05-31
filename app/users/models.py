from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser): 
    is_doctor = models.BooleanField(blank=False, default=False)
    is_lab_staff = models.BooleanField(blank=False, default=False)
    is_clerical_staff = models.BooleanField(blank=False, default=True) # we're assuming that by default all accounts are for clerical staffs
    

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])