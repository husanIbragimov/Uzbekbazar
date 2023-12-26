from django.contrib import admin
from .models import Wishlist, ShopCart, Order, OrderItem, OrderOneClick, OrderVariant, OrderInfo
from app.products.models import ProductSize
from import_export.admin import ImportExportModelAdmin
from app.products.resource import ProductSizeResource


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 1
    # list_display = ['order', 'product', "quenty", 'product_image', 'product_size']
    


       
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemAdmin]
    list_display = ['uuid', 'user', 'phone_number', 'status']
    readonly_fields = ['uuid', 'user', 'phone_number']
    
    
    
@admin.register(OrderOneClick)
class OrderOneClickAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',  'phone_number', 'status']
    readonly_fields = ['first_name', 'last_name', 'phone_number']
    
    
    
@admin.register(OrderVariant)
class OrderVariantAdmin(admin.ModelAdmin):
    list_display = ['user', 'status', 'variant']



@admin.register(ProductSize)
class ProductImageAdmin(ImportExportModelAdmin):
    list_display = ("product", "color", "size", "availability", "price")
    resource_classes = [ProductSizeResource]
    list_editable = ["availability", "price"]


admin.site.register(Wishlist)
admin.site.register(ShopCart)
admin.site.register(OrderInfo)
