from modeltranslation.translator import register, TranslationOptions
from .models import (
    Category,
    Size,
    Season,
    Colors,
    Brend,
    Banner,
    AuthorBook,
    CoverBook,
    PublisherBook,
    LanguageBook,
    Tags,
    Additional_info,
    BannerDiscount,
    DiscountDate,
    MonthlyBestSell,
    BannerBottom,
    Product,
    Volume_Xajm
)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    
    
@register(Season)
class SeasonTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    
    
@register(Size)
class SizeTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    
@register(Colors)
class ColorsTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    
    
@register(Brend)
class BrendTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    
    
@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    

@register(AuthorBook)
class AuthorBookTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    
@register(CoverBook)
class CoverBookTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    
@register(PublisherBook)
class PublisherBookTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    
    
@register(LanguageBook)
class LanguageBookTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    
@register(Tags)
class TagsTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    
    
@register(Additional_info)
class Additional_infoTranslationOptions(TranslationOptions):
    fields = (
        'key',
        'value'
    )
    
@register(BannerDiscount)
class BannerDiscountTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )

@register(DiscountDate)
class DiscountDateTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    
@register(MonthlyBestSell)
class MonthlyBestSellTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    
@register(BannerBottom)
class BannerBottomTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    
    
@register(Volume_Xajm)
class Volume_XajmTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
    
    
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'desc',
        'description'
    )