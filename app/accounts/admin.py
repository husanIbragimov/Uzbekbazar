from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Organization, Contract, Tariff
from django.utils.translation import gettext as _


# Register your models here.
@admin.register(User)
class ModelNameAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "photo")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class ContractItemAdmin(admin.StackedInline):
    model = Contract
    extra = 1

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [ContractItemAdmin]


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(organization = request.user.organization)
        return queryset
