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
    banner = models.FileField(upload_to="Organizations", null=True, blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='organization',
    )
    telegram_group_id = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.name


class Tariff(BaseModel):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Contract(BaseModel):
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE, related_name='organization')
    company_type = models.CharField(max_length=2555, verbose_name='firma turi')
    mfo = models.CharField(max_length=50, null=True, blank=True, verbose_name='mfo')
    oked = models.CharField(max_length=50, null=True, blank=True, verbose_name='oked')
    inn = models.CharField(max_length=20, verbose_name='inn')
    statute = models.FileField(upload_to='ustav/', verbose_name='ustav')
    certificate = models.FileField(upload_to='guvohnoma/', name='guvohnoma')
    director_passport = models.FileField(upload_to='director_passport/', verbose_name='direktor pasport')
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE, related_name='organization')

    def __str__(self) -> str:
        return self.organization.name
