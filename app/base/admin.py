from django.contrib import admin
from .models import Variant
from mptt.admin import DraggableMPTTAdmin

# Register your models here.

@admin.register(Variant)
class VariantAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title', 'name', 'description', 'duration', 'percent', 'is_active')
    
    search_fields = ('name',)
    list_per_page = 25