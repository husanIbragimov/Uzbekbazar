from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Organization
# Register your models here.
@admin.register(User)
class ModelNameAdmin(UserAdmin):
    pass

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', )