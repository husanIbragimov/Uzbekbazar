from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.contrib import messages
from .models import (
    Banner,
    BannerDiscount,
    DiscountDate,
    Brend,
    MonthlyBestSell,
    BannerBottom,
    Product,
    Category,
    Colors,
    Size,
    Season,
    AuthorBook,
    CoverBook,
    PublisherBook,
    LanguageBook,
    ProductReview,
    ProductImage
)
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.core.paginator import Paginator
from .forms import ProductReviewForm
from django.db.models import Q
import uuid
from django.http import HttpResponseNotFound
from django.core.cache import cache
# Create your views here.
class HomePage(View):
    DEFAULT_TIMEOUT = 60*2
    def get(self, request):
        product = cache.get('product') 
        banner_discount = cache.get('banner_discount')
        banner_bottom = cache.get('banner_bottom')
        banners = cache.get('banners')
        if product or banner_discount or banner_bottom or banners :
            pass
        else:
            banner_discount = BannerDiscount.objects.all().last()
            product = Product.objects.filter(is_active=True).order_by('?')[:20]
            banner_bottom = BannerBottom.objects.filter(is_active=True).last()
            banners = Banner.objects.filter(is_active=True).order_by('-create_at')[:3]
            cache.set('product', product, self.DEFAULT_TIMEOUT)
            cache.set('banner_discount', banner_discount, self.DEFAULT_TIMEOUT)
            cache.set('banner_bottom', banner_bottom, self.DEFAULT_TIMEOUT)
            cache.set('banners', banners, self.DEFAULT_TIMEOUT)
        
        discount_date = DiscountDate.objects.filter(deadline__gte=datetime.now(), is_active=True).order_by('-create_at')[:2]
        brend = Brend.objects.filter(is_active=True).order_by('-create_at')
        monthly_best_sell = MonthlyBestSell.objects.filter(is_active=True).order_by('-create_at')[:2]
        popular_product = Product.objects.filter(is_active=True).order_by('?')[:20]
        new_products = Product.objects.filter(is_active=True).order_by('-create_at')[:20]
        hot_products = Product.objects.filter(is_active=True, status='hot').order_by('-create_at')[:3]
        best_products = Product.objects.filter(is_active=True, status='best').order_by('-create_at')[:3]
        
        
        context = {
            'banners' : banners,
            'banner_discount' : banner_discount,
            'discount_date' : discount_date,
            'brend' : brend,
            'monthly_best_sell' : monthly_best_sell,
            'banner_bottom' : banner_bottom,
            'product' : product,
            'popular_product': popular_product,
            'new_products' : new_products,
            'hot_products' : hot_products,
            'best_products' : best_products
        }
        return render(request, 'index.html', context)
    
    
    
class ShopView(View):
   
    def get(self, request, uuid):
        
        products = Product.objects.filter(category__uuid = uuid, is_active=True)
        category = Category.objects.get(uuid = uuid, is_active=True)
        new_products = Product.objects.filter(category__uuid = uuid, is_active=True).order_by('-create_at')[:3]
        monthly_best_sell = MonthlyBestSell.objects.filter(is_active=True).last()
        brend = Brend.objects.filter(is_active=True, category__uuid = uuid).order_by('-create_at')
        colors = Colors.objects.filter(is_active=True).order_by('-create_at')
        if category.is_size:
            size = Size.objects.get(uuid = category.is_size.uuid, is_active=True).get_children()
        else:
            size = None
        season = Season.objects.filter(is_active=True).order_by('-create_at')
        authbook = AuthorBook.objects.filter(is_active=True).order_by('-create_at')
        coverbook = CoverBook.objects.filter(is_active=True).order_by('-create_at')
        publisherbook = PublisherBook.objects.filter(is_active=True).order_by('-create_at')
        languagebook = LanguageBook.objects.filter(is_active=True).order_by('-create_at')

        page_size = request.GET.get('page_size', 30)
        paginator = Paginator(products, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        
        if category.parent:
            sub_cat = category
            category = category.parent.parent
        else:
            sub_cat = None
        context = {
            'category' : category,
            'products' : page_obj,
            'sub_cat' : sub_cat,
            'new_products' : new_products,
            'monthly_best_sell' : monthly_best_sell,
            'brend' : brend,
            'colors' : colors,
            'size' : size,
            'season' : season,
            'authbook' : authbook,
            'coverbook' : coverbook,
            'publisherbook' : publisherbook,
            'languagebook' : languagebook,
            'filter_request': {}
        }
        return render(request, 'shop.html', context)
    
    def post(self, request, uuid):
        filter_request = {
            'color' : list(map(int, request.POST.getlist('color'))),
            'size' : list(map(int, request.POST.getlist('size'))),
            'season' : list(map(int, request.POST.getlist('season'))),
            'authbook' : list(map(int, request.POST.getlist('authbook'))),
            'coverbook' : list(map(int, request.POST.getlist('coverbook'))),
            'publisherbook' : list(map(int, request.POST.getlist('publisherbook'))),
            'languagebook' : list(map(int, request.POST.getlist('languagebook'))),
        }
        products = Product.objects.filter(category__uuid = uuid, is_active=True)
        category = Category.objects.get(uuid = uuid, is_active=True)
        new_products = Product.objects.filter(category__uuid = uuid, is_active=True).order_by('-create_at')[:3]
        monthly_best_sell = MonthlyBestSell.objects.filter(is_active=True).last()
        brend = Brend.objects.filter(is_active=True, category__uuid = uuid).order_by('-create_at')
        colors = Colors.objects.filter(is_active=True).order_by('-create_at')
        size = Size.objects.filter(is_active=True).order_by('-create_at')
        season = Season.objects.filter(is_active=True).order_by('-create_at')
        authbook = AuthorBook.objects.filter(is_active=True).order_by('-create_at')
        coverbook = CoverBook.objects.filter(is_active=True).order_by('-create_at')
        publisherbook = PublisherBook.objects.filter(is_active=True).order_by('-create_at')
        languagebook = LanguageBook.objects.filter(is_active=True).order_by('-create_at')
         
     
        
        
        
        if (filter_request.get('season') or filter_request.get('authbook') or filter_request.get('coverbook')  or 
            filter_request.get('publisherbook')  or filter_request.get('languagebook') or filter_request.get('color') or filter_request.get('size')) :
            products = products.filter(
                Q(season__in=filter_request.get('season')) | Q(author_book__in=filter_request.get('authbook')) | Q(cover_book__id__in=filter_request.get('coverbook')) | Q(publisher_book__id__in=filter_request.get('publisherbook'))  | Q(language_book__id__in=filter_request.get('languagebook')) |
                Q(product_size__color__in=filter_request.get('color')) | Q(product_size__size__in=filter_request.get('size')) 
            ) 
            
            
  
       
      
        clear_products = products.distinct('uuid')
    

        page_size = request.GET.get('page_size', 10)
        paginator = Paginator(clear_products, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        
        if category.is_size:
            size = Size.objects.get(uuid = category.is_size.uuid, is_active=True).get_children()
        else:
            size = None
            
        if category.parent:
            sub_cat = category
            category = category.parent.parent
        else:
            sub_cat = None
     
        
        context = {
            'category' : category,
            'products' : page_obj,
            'sub_cat' : sub_cat,
            'new_products' : new_products,
            'monthly_best_sell' : monthly_best_sell,
            'brend' : brend,
            'colors' : colors,
            'size' : size,
            'season' : season,
            'authbook' : authbook,
            'coverbook' : coverbook,
            'publisherbook' : publisherbook,
            'languagebook' : languagebook,
            'filter_request': filter_request
        }
        return render(request, 'shop.html', context)
        
    
class ShopViewAll(View):
    def get(self, request):
        products = Product.objects.filter(is_active=True).order_by('?')
        
        context = {
            'products' : products
        }
        return render(request, 'shopall.html', context)

class ShopDetailView(View):
    def get(self, request, slug, uuidd):
        
            product = get_object_or_404(Product, uuid=uuidd, is_active=True)
            
            banner_discount = BannerDiscount.objects.filter(is_active=True).last()
            productreview = product.praducts_review.all().order_by("-create_at")
            image = product.product_images.all()
            image_color = ProductImage.objects.filter(product__uuid = uuidd, is_active=True)
            praducts_additional_info = product.praducts_additional_info.all()
            related_products_all = product.category.all()
            category_data = []
            for related_product in related_products_all:
                category = Category.objects.get(uuid = related_product.uuid)
                for product_category in category.category_products.all():
                    if product_category not in category_data:
                        category_data.append(product_category)
            image_color_data = []
            color_id = []
            
            if product.cover_book:
                pass
            else:
                for image_col in image_color:
                    if image_col.color.id in color_id:
                        pass
                    else:
                        color_id.append(image_col.color.id)
                        image_color_data.append(ProductImage.objects.get(id=image_col.id, is_active=True))
            
            
            tags_seao = ''
            tags = product.tags.all()
            
            for tag in tags:
                tags_seao += f'{tag} '

            
            active_color = request.GET.get('color', product.product_size.first().color.uuid)
            active_variant = request.GET.get('variant', 0)

            if active_color:
                active_size = request.GET.get('size', product.product_size.filter(Q(color__uuid__icontains = active_color) & Q(is_active=True))[0].size.uuid)
                
                
        
                if active_size:
                    product_price = product.product_size.filter(Q(color__uuid__icontains = active_color) & Q(size__uuid__icontains = active_size) & Q(is_active=True))[0].price
                    product_availability = product.product_size.filter(Q(color__uuid__icontains = active_color) & Q(size__uuid__icontains = active_size) & Q(is_active=True))[0].availability
                else:
                    product_price = product.product_size.filter(color__uuid = active_color, is_active=True)[0].price
                    
                    product_availability = product.product_size.filter(color__uuid = active_color, is_active=True)[0].availability
            
                
                        
                
                product_size = product.product_size.filter(color__uuid = active_color, is_active=True)

                
            else:
                product_price = product.product_size.first().price
                product_availability = product.product_size.first().availability
                product_size = product.product_size.filter(color__uuid = product.product_images.first().color.uuid, is_active=True)
                
                
                
                
            if product.percentage:
                product_discount_price = product_price - (product_price*product.percentage)/100
            else:
                product_discount_price = 0
                
                
            
            page_size = request.GET.get('page_size', 5)
            paginator = Paginator(productreview, page_size)

            page_num = request.GET.get('page', 1)
            page_obj = paginator.get_page(page_num)
            context = {
                'product' : product,
                'productreview_all' : productreview,
                'productreview' : page_obj,
                'images' : image,
                'image_color_data' : image_color_data,
                'product_size' : product_size,
                'tags' : tags,
                'tags_seao' : tags_seao,
                'related_products' : category_data,
                'praducts_additional_info' : praducts_additional_info,
                'product_price' : product_price,
                'product_discount_price' : product_discount_price,
                'active_color' : uuid.UUID(str(active_color)),
                'active_size' : uuid.UUID(str(active_size)),
                'active_variant' : int(active_variant),
                'product_availability' : product_availability,
                'banner_discount' : banner_discount

            }

            return render(request, 'shop-product-detail.html',context)
    
       
    
       
class ProductCommentView(LoginRequiredMixin, View):
    form_class = ProductReviewForm
    def post(self, request, uuid):
        url = request.META.get('HTTP_REFERER')
        
        product = Product.objects.get(uuid=uuid)
        form = self.form_class(
            data=request.POST,
            files=request.FILES
        )
        
        if form.is_valid():
            ProductReview.objects.create(
                user = request.user,
                product = product,
                comment = form.cleaned_data['comment'],
                image = form.cleaned_data['image'],
                stars = form.cleaned_data['stars']
            )
            messages.success(request, 'Comment muvafaqiyatli yuborildi')
            return redirect(url)
        messages.error(request, f'{form.errors}')
        return redirect('/')
    
    
class SearchResultsView(View):
    def get(self, request):
        query = request.GET.get("search")
        object_list = Product.objects.filter(
            Q(title__icontains=query) | Q(desc__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query)
        ) 
        
        context = {
            'products' : object_list.distinct('uuid')
        }
        
        return render(request, 'shopall.html', context)
