from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='profile/', default='profile/profile.svg')

    def save(self, *args, **kwargs):
        # Auto-generate username based on phone number
        if self.username:
            self.phone = self.username
        super().save(*args, **kwargs)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username