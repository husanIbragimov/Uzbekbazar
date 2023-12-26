from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# from django.contrib.auth.models import User
from app.base.models import BaseModel, Variant
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.db.models import Avg

# Create your models here.


STATUS = (
    ('new', 'NEW'),
    ('hot', 'HOT'),
    ('best', 'BEST SELL'),
    ('sale', 'SALE'),
)


class Size(MPTTModel, BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Razmer"
        verbose_name_plural = "Razmerlar"

    def __str__(self):
        return self.name
    
class Category(MPTTModel, BaseModel):
    
    name = models.CharField(max_length=255, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    icon = models.FileField(upload_to='icon/', null=True, blank=True)
    photo = models.ImageField(upload_to='banner/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_colors = models.BooleanField(default=False)
    is_brend = models.BooleanField(default=False)
    is_size = models.ForeignKey(Size,null=True, blank=True, on_delete=models.CASCADE, related_name='category_size')
    is_season = models.BooleanField(default=False)
    is_authorBook = models.BooleanField(default=False)
    is_coverBook = models.BooleanField(default=False)
    is_publisherBook = models.BooleanField(default=False)
    is_languageBook = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Colors(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Rang"
        verbose_name_plural = "Ranglar"
    def __str__(self):
        return  self.name




class Brend(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True,
                                      limit_choices_to={'is_active': True}, related_name='category_brend')
    photo = models.ImageField(upload_to='brend/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Brend"
        verbose_name_plural = "Brendlar"

    def __str__(self):
        return  self.name



class Season(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Mavsum"
        verbose_name_plural = "Mavsumlar"

    def __str__(self):
        return self.name


class AuthorBook(BaseModel): #For book
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Kitob Muallif"
        verbose_name_plural = "Kitob Mualliflar"

    def __str__(self):
        return  self.name

class CoverBook(BaseModel): #For book
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Kitob Muqova"
        verbose_name_plural = "Kitob Muqovalar"

    def __str__(self):
        return  self.name


class PublisherBook(BaseModel): #For book
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Kitob Nashriyoti"
        verbose_name_plural = "Kitob Nashriyotlar"

    def __str__(self):
        return  self.name


class LanguageBook(BaseModel): #For book
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Kitob tili"
        verbose_name_plural = "Kitob tililar"

    def __str__(self):
        return  self.name



class Tags(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Volume_Xajm(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name


class Product(BaseModel):
    category = models.ManyToManyField(Category,  blank=True,
                                      limit_choices_to={'is_active': True}, related_name='category_products')
    title = models.TextField()
    slug = models.SlugField(max_length=250)
    status = models.CharField(choices=STATUS, max_length=10, null=True, blank=True)
    brand = models.ForeignKey(Brend, on_delete=models.CASCADE, null=True, blank=True, related_name='brand_products')
    desc = RichTextUploadingField()
    tags = models.ManyToManyField(Tags,blank=True, related_name='tags_products')
    
    description = RichTextUploadingField()
    price_default = models.IntegerField(null=True, blank=True, default=0)
    percentage = models.FloatField(default=0, null=True, blank=True)
    discount = models.FloatField(default=0, null=True, blank=True)
    season = models.ManyToManyField(Season, blank=True, related_name='season_products') # for clothes
    author_book = models.ManyToManyField(AuthorBook, blank=True, related_name='author_book_products') #for book
    publisher_book = models.ForeignKey(PublisherBook, on_delete=models.SET_NULL, null=True, blank=True, related_name='publisher_book_products') #for book
    language_book = models.ForeignKey(LanguageBook, on_delete=models.SET_NULL, null=True, blank=True, related_name='language_book_products') #for book
    cover_book = models.ForeignKey(CoverBook, on_delete=models.CASCADE, related_name='cover_products', null=True, blank=True) #for book
    variant = models.ManyToManyField(Variant, blank=True, related_name='variant_products')
    volume_xajm = models.ForeignKey(Volume_Xajm,  on_delete=models.SET_NULL, null=True, blank=True, related_name='valume_products')
    volume_xajm_value = models.IntegerField(null=True, blank=True, default=0)
    is_active = models.BooleanField(default=True)
    
    
  
    @property
    def mid_stars(self):
        result = ProductReview.objects.filter(product=self.id).aggregate(avarage=Avg("stars"))
        if result['avarage']:
            return round(result['avarage'], 1)
        else:
            return 0

    @property
    def mid_stars_percent(self):
        result = ProductReview.objects.filter(product=self.id).aggregate(avarage=Avg("stars"))
        if result['avarage']:
            percent = result['avarage'] * 100 / 5
            return int(percent)
        else:
            return 0

    @property
    def get_discount_price(self):
        if self.percentage:
            discount_sell = self.product_size.first().price - (
                    self.product_size.first().price * (self.percentage / 100))
            return discount_sell
        return 0

    @property
    def get_price(self):

        return self.product_size.first().price
    
 


    def __str__(self):
        if self.title:
            return self.title
        return f'{self.id}'

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images', null=True, blank=True)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE, related_name='product_images', null=True, blank=True)
    image = models.FileField(upload_to='products', null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Color {self.color} --- {self.image}'

    @property
    def image_url(self):
        return self.image.url

class ProductSize(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_size', null=True, blank=True)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE, related_name='product_size', null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='product_size', null=True, blank=True)
    availability = models.BigIntegerField(null=True, blank=True)
    price = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    

    
    def __str__(self):
        return f'{self.product}'

class Additional_info(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='praducts_additional_info')
    key = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.key} - {self.value}'

class ProductReview(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='praducts_review')
    product= models.ForeignKey(Product, on_delete=models.CASCADE, related_name='praducts_review')
    comment = models.TextField()
    image = models.ImageField(upload_to='comment/', null=True, blank=True)
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = "Commentlar"
    def __str__(self):
        return self.comment

    @property
    def stars_percent(self):
        return round(int(self.stars * 100 / 5), 1)

class Banner(BaseModel):
    name = RichTextUploadingField()
    photo = models.ImageField(upload_to='banner/', null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True, related_name='products_banner')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Asosiy Banner"
        verbose_name_plural = "Asosiy Bannerlar"

    def __str__(self):
        return self.name



class BannerDiscount(BaseModel):
    name = RichTextUploadingField()
    photo = models.ImageField(upload_to='banner_discount/', null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True, related_name='products_banner_discount')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Chegirmalar uchun banner"
        verbose_name_plural = "Chegirmalar uchun bannerlar"

    def __str__(self):
        return self.name


class DiscountDate(BaseModel):
    name = RichTextUploadingField()
    photo = models.ImageField(upload_to='discount_data/', null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True, related_name='products_discount_date')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Vaqt bilan beriladigon chegirma"
        verbose_name_plural = "Vaqt bilan beriladigon chegirmalar"
    def __str__(self):
        return self.name


class MonthlyBestSell(BaseModel):
    name = RichTextUploadingField()
    photo = models.ImageField(upload_to='monthly_best_sell/', null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True, related_name='products_monthly_best_sell')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Oylik eng kop sotilgan"
        verbose_name_plural = "Oylik eng kop sotilganlar"

    def __str__(self):
        return self.name


class BannerBottom(BaseModel):
    name = RichTextUploadingField()
    photo = models.ImageField(upload_to='banner_bottom/', null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True, related_name='products_banner_bottom')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Pastgi Banner"
        verbose_name_plural = "Pastgi Bannerlar"

    def __str__(self):
        return self.name

