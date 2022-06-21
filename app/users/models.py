from email.policy import default
from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.urls import reverse
import uuid

class CustomUser(AbstractUser): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_doctor = models.BooleanField(blank=True, default=False)
    is_lab_staff = models.BooleanField(blank=True, default=False)
    is_clerical_staff = models.BooleanField(blank=True, default=False)

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])