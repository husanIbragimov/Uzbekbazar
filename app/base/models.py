from django.db import models
from django.utils import timezone
import datetime
import uuid 
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(default = uuid.uuid4, 
         editable = False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Variant(MPTTModel, BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(default=0)
    percent = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.description