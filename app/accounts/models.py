from django.db import models
from django.contrib.auth.models import AbstractUser
from app.base.models import BaseModel

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


class Organization(BaseModel):
    name = models.CharField(max_length=255)
    avatar = models.FileField(upload_to="Organizations", null=True, blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='organization',
    )
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
