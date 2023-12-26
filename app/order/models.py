from django.db import models
from app.base.models import BaseModel
from django.db.models import Q

# Create your models here.
class Wishlist(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='whitelist_user')
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name='whitelist_product')

    def __str__(self):
        return self.user.username
    

class ShopCart(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='cart_user')
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name='cart_product')
    quenty = models.IntegerField(default=1)
    product_image = models.ForeignKey("products.ProductImage", on_delete=models.SET_NULL, null=True, blank=True, related_name='cart_image')
    product_size = models.ForeignKey("products.Size", on_delete=models.SET_NULL, null=True, blank=True, related_name='cart_size')
    product_color = models.ForeignKey("products.Colors", on_delete=models.SET_NULL, null=True, blank=True, related_name='cart_color')
    product_price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username

class Order(BaseModel):
    STATUS = (
        ('New', 'New'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='order_user')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    
    def save(self, *args, **kwargs):
        if self.status == "Completed":
            for order_it in self.order_item.all():
                order_it.product.product_size.filter(Q(color = order_it.product_color) & Q(size = order_it.product_size) & Q(is_active=True)).update(
                    availability = order_it.product.product_size.get(Q(color = order_it.product_color) & Q(size = order_it.product_size) & Q(is_active=True)).availability - order_it.quenty
                )

        super().save(*args, **kwargs)
    def __str__(self):
        if self.phone_number:
            return f"{self.phone_number}"
        return self.user.username
    

class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name='order_product')
    quenty = models.IntegerField(default=1)
    product_image = models.ForeignKey("products.ProductImage", on_delete=models.SET_NULL, null=True, blank=True, related_name='order_image')
    product_size = models.ForeignKey("products.Size", on_delete=models.SET_NULL, null=True, blank=True, related_name='order_size')
    product_color = models.ForeignKey("products.Colors", on_delete=models.SET_NULL, null=True, blank=True, related_name='order_color')
    product_price = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.order.user.username
    
    
class OrderOneClick(BaseModel):
    STATUS = (
        ('New', 'New'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    
    first_name = models.CharField(max_length=255, null=True )
    last_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name='order_one_click_product')
    product_image = models.ForeignKey("products.ProductImage", on_delete=models.SET_NULL, null=True, blank=True, related_name='order_one_click_image')
    color = models.ForeignKey('products.Colors', on_delete=models.CASCADE)
    size = models.ForeignKey('products.Size', on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    
    def save(self, *args, **kwargs):
        if self.status == "Completed":
            self.product.product_size.filter(Q(color = self.color) & Q(size = self.size) & Q(is_active=True)).update(availability = self.product.product_size.get(Q(color = self.color) & Q(size = self.size) & Q(is_active=True)).availability - 1)

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.phone_number}"
    
class OrderVariant(BaseModel):
    STATUS = (
        ('New', 'New'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='order_variant_user')
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name='order_variant_product')
    product_image = models.ForeignKey("products.ProductImage", on_delete=models.SET_NULL, null=True, blank=True, related_name='order_variant_image')
    color = models.ForeignKey('products.Colors', on_delete=models.CASCADE)
    size = models.ForeignKey('products.Size', on_delete=models.CASCADE)
    variant = models.ForeignKey('base.Variant', on_delete=models.CASCADE)
    price = price = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
            # Auto-generate username based on phone number
        product_price = self.product.product_size.filter(Q(color = self.color) & Q(size = self.size) & Q(is_active=True))[0].price
        if self.product.percentage:
            product_price = product_price - (product_price*self.product.percentage)/100
            price = (product_price + (product_price*self.variant.percent)/100)/self.variant.duration
        else:
            price = (product_price + (product_price*self.variant.percent)/100)/self.variant.duration
        
        self.price = price
        
        if self.status == "Completed":
            self.product.product_size.filter(Q(color = self.color) & Q(size = self.size) & Q(is_active=True)).update(availability = self.product.product_size.get(Q(color = self.color) & Q(size = self.size) & Q(is_active=True)).availability - 1)

        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.user.username
    
class OrderInfo(BaseModel):
    STATUS = (
        ('New', 'New'),
        ('Completed', 'Completed'),
    )
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='order_info_user')
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name='order_info_product')
    product_image = models.ForeignKey("products.ProductImage", on_delete=models.SET_NULL, null=True, blank=True, related_name='order_info_image')
    product_size = models.ForeignKey('products.ProductSize', on_delete=models.CASCADE, null=True, blank=True, related_name='order_info_size')
    
    def __str__(self):
        return self.user.username