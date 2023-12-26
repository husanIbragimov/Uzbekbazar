from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views import View
from app.products.models import Product
from django.http import JsonResponse
from .models import Wishlist, ShopCart, Order, OrderItem, OrderOneClick, OrderVariant, OrderInfo
from app.products.models import ProductImage, Size, Colors
from app.base.models import Variant
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderOneClickForm
from django.urls import reverse
from django.db.models import Q
from bot.main import order_product_one_clik, order_product_variant, order_product_shop, order_product_info
import asyncio

# Create your views here.

class WithListUuidView(LoginRequiredMixin, View):
    def get(self, request, uuid):
        url = request.META.get('HTTP_REFERER')
        product = get_object_or_404(Product, uuid=uuid)
        user = request.user
        if Wishlist.objects.filter(user=user, product=product).exists():
            messages.info(request, "Siz tanlagan mahsulot yoqtirganlar ro'yxatiga qo'shilgan")
            return redirect(url)
        else:
            Wishlist.objects.create(
                user = user,
                product = product
            )
            messages.success(request, "Siz tanlagan mahsulot yoqtirganlar ro'yxatiga qo'shildi")
            return redirect(url)
        
              
class WithListView(LoginRequiredMixin, View):
    def get(self, request):
        wishlist = Wishlist.objects.filter(user = request.user)
        context = {
            'wishlist' : wishlist
        }
        
        return render(request, 'shop-wishlist.html', context)
        
        
class WishListDeleteView(LoginRequiredMixin, View):
    def get(self, request, uuid):
        url = request.META.get('HTTP_REFERER')
        Wishlist.objects.get(uuid=uuid).delete()
        messages.success(request, "Siz tanlagan mahsulot yoqtirganlar ro'yxatidan olib taylandi")
        return redirect(url)
    
    
class ShopCartListView(LoginRequiredMixin, View):
    def get(self, request):
        shopcart = ShopCart.objects.filter(user = request.user)
        context = {
            'shopcart' : shopcart
        }
        return render(request, 'shop-cart.html', context)


class ShopCartDeleteView(LoginRequiredMixin, View):
    def get(self, request, uuid):
        url = request.META.get('HTTP_REFERER')
        ShopCart.objects.get(uuid=uuid).delete()
        messages.success(request, "Siz tanlagan mahsulot savatchadan olib taylandi")
        return redirect(url)
    
class ShopCartDeleteAllView(LoginRequiredMixin, View):
    def get(self, request):
        url = request.META.get('HTTP_REFERER')
        ShopCart.objects.filter(user=request.user).delete()
        messages.success(request, "Siz tanlagan mahsulotlar savatchadan olib taylandi")
        return redirect(url)
    
    
class ShopCartAddOneView(LoginRequiredMixin, View):
    def get(self, request, uuid):
        url = request.META.get('HTTP_REFERER')
        product = get_object_or_404(Product, uuid=uuid)
        user = request.user
        
        if ShopCart.objects.filter(user=user, product=product).exists():
            messages.info(request, "Siz tanlagan mahsulot savatchaga qo'shilgan")
            return redirect(url)
        else:
            
            product_size = product.product_size.first().size,
            product_color = product.product_size.first().color,
            product_price = product.product_size.filter(Q(color = product_color[0]) & Q(size = product_size[0]) & Q(is_active=True))[0].price
            product_image = product.product_images.filter(color = product_color[0])[0]
            quenty = 1
            if product.percentage:
                product_price = product_price - (product_price*product.percentage)/100
            
            ShopCart.objects.create(
                user = user,
                product = product,
                quenty = quenty,
                product_image = product_image,
                product_size = product_size[0],
                product_color = product_color[0],
                product_price = product_price,
            )
            messages.success(request, "Siz tanlagan mahsulot savatchaga qo'shildi")
            return redirect(url)
        
    def post(self, request, uuid):
        url = request.META.get('HTTP_REFERER')
        product = get_object_or_404(Product, uuid=uuid)
        user = request.user
        quenty = request.POST.get('quantity')
        product_color_uuid = request.POST.get('active_color')
        product_size_uuid = request.POST.get('active_size')
        
        product_size = product.product_size.filter(size__uuid = product_size_uuid)[0].size,
        product_color = product.product_size.filter(color__uuid = product_color_uuid)[0].color,
        
        
        product_price = product.product_size.filter(Q(color = product_color[0]) & Q(size = product_size[0]) & Q(is_active=True))[0].price
        if product.percentage:
            product_price = product_price - (product_price*product.percentage)/100
        
        
        product_image = product.product_images.filter(color__uuid = product_color_uuid)[0]
    
        ShopCart.objects.create(
                user = user,
                product = product,
                quenty = quenty,
                product_image = product_image,
                product_size = product_size[0],
                product_color = product_color[0],
                product_price = product_price,
            )
        messages.success(request, "Siz tanlagan mahsulot savatchaga qo'shildi")
        return redirect(url)
        

    
    
class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        
        url = request.META.get('HTTP_REFERER')
        shop_cart = ShopCart.objects.filter(user = request.user)
        if shop_cart:
            for shop_cat in shop_cart:
                if shop_cat.product.product_size.get(Q(color = shop_cat.product_color) & Q(size = shop_cat.product_size) & Q(is_active=True)).availability:
                    order = Order.objects.create(
                        user = request.user,
                        phone_number = request.user.phone
                    )
                    data = []
                    for shop_cart_item in shop_cart:
                        data.append(OrderItem(order=order, product=shop_cart_item.product, quenty = shop_cart_item.quenty, product_image = shop_cart_item.product_image, product_size = shop_cart_item.product_size, product_color=shop_cart_item.product_color, product_price=shop_cart_item.product_price))
                    OrderItem.objects.bulk_create(data, batch_size=100)
                    shop_cart.delete()
                    context = {
                        "order" : order
                    }
                    
                    order_item = []
                    for i in order.order_item.all():
                        order_item.append(
                            dict(
                                product = i.product.title,
                                quenty = i.quenty,
                                product_image = i.product_image.image.url,
                                product_size = i.product_size.name,
                                product_color = i.product_color.name,
                                product_price = i.product_price
                            )
                        )
                    asyncio.run(order_product_shop(order, order_item))
                    return render(request, 'order-confirmed-shop.html', context)
                else:
                    messages.info(request, 'Siz Tanlagan mahsulot Xozir qolmagan')
                    return redirect(url)
        return redirect(reverse("accounts:profile"))
    
    
class OrderCreateOneClikView(View):
    form_class = OrderOneClickForm
    def get(self, request, uuid):
        try: 
            product =get_object_or_404(Product, uuid=uuid)
            current_color = request.GET.get('color')
            current_size = request.GET.get('size')
            color = get_object_or_404(Colors, uuid=current_color)
            size = get_object_or_404(Size, uuid=current_size)
            
            product_price = product.product_size.filter(Q(color = color) & Q(size = size) & Q(is_active=True))[0].price
            if product.percentage:
                product_price = product_price - (product_price*product.percentage)/100
          
            context = {
                'product' : product,
                'size' : size,
                'color' : color, 
                'product_price' : product_price,
                'product_image' : product.product_images.filter(Q(color = color))[0]
            }
            
            return render(request, 'checkout.html', context)
        except Exception as e:
            return redirect('/')
    
    def post(self, request, uuid):
        url = request.META.get('HTTP_REFERER')
        
        product =get_object_or_404(Product, uuid=uuid)
        color = get_object_or_404(Colors, uuid=request.POST.get('color'))
        size = get_object_or_404(Size, uuid=request.POST.get('size'))
        if product.product_size.get(Q(color = color) & Q(size = size) & Q(is_active=True)).availability:
            product_price = product.product_size.filter(Q(color = color) & Q(size = size) & Q(is_active=True))[0].price
            if product.percentage:
                product_price = product_price - (product_price*product.percentage)/100
        
            form = self.form_class(data=request.POST)
            
            if form.is_valid():
                order = OrderOneClick.objects.create(
                    first_name = form.cleaned_data['first_name'],
                    last_name = form.cleaned_data['last_name'],
                    phone_number = form.cleaned_data['phone_number'],
                    color = color,
                    size = size,
                    price=product_price,
                    product = product,
                    product_image = product.product_images.filter(Q(color = color))[0]
                )
                context = {
                    'order' : order
                }

                asyncio.run(order_product_one_clik(order))
                return render(request, 'order-confirmed.html', context)
            
        else:
            messages.info(request, 'Siz Tanlagan mahsulot Xozir qolmagan')
            return redirect(url)
        
        messages.error(request, f'{form.errors}')
        return redirect('/')
    
 
class OrderVariantView(LoginRequiredMixin, View):
    def get(self, request, uuid):
        url = request.META.get('HTTP_REFERER')
        
        return redirect('/')
    
    def post(self, request, uuid):
        url = request.META.get('HTTP_REFERER')
        product = get_object_or_404(Product, uuid=uuid, is_active=True)
        current_color = request.POST.get('active_color')
        current_size = request.POST.get('active_size')
        current_variant = request.POST.get('active_variant')
        if int(current_variant) == 0:
            messages.info(request, 'Muddatli tulovga xarid qilish uchun variant tanlang')
            return redirect(url)
        else:
            order = OrderVariant.objects.create(product=product, user=request.user, color = Colors.objects.get(uuid=current_color), size = Size.objects.get(uuid=current_size), variant = Variant.objects.get(id=current_variant), product_image = product.product_images.filter(Q(color = Colors.objects.get(uuid=current_color)))[0])
            context = {
                'order' : order
            }
            asyncio.run(order_product_variant(order))
            return render(request, 'order-confirmed-variant.html', context)
        
        
class OrderCreateInfoView(LoginRequiredMixin, View):
    def get(self, request, uuid):
        url = request.META.get('HTTP_REFERER')
        
        product = get_object_or_404(Product, uuid=uuid)
        current_color = request.GET.get('color')
        current_size = request.GET.get('size')
        color = get_object_or_404(Colors, uuid=current_color)
        size = get_object_or_404(Size, uuid=current_size)
        
        try:

            order = OrderInfo.objects.get(user = request.user, product = product)
            messages.success(request, "Siz tanlagan mahsulot yetib kelishi bilan siz bilan bog'lanamiz")    

        except Exception as e:
            order = OrderInfo.objects.create(
                user = request.user,
                product = product,
                product_image =  product.product_images.filter(Q(color = color))[0],
                product_size = product.product_size.filter(size = size, color = color)[0]
                )
            messages.success(request, "Siz tanlagan mahsulot yetib kelishi bilan siz bilan bog'lanamiz")    
            
            asyncio.run(order_product_info(order))
        return redirect(url)


class NotificationView(LoginRequiredMixin, View):
    def get(self, request):
        order_info = OrderInfo.objects.filter(user = request.user, status='Completed')
        context = {
            'order_info' : order_info
        }
        return render(request, 'shop-notifications.html', context)


class OrderInfoDeleteView(View):
    def get(self, request, uuid):
        url = request.META.get('HTTP_REFERER')
        OrderInfo.objects.get(uuid=uuid).delete()
        return redirect(url)
