from django.urls import path
from .views import HomePage, ShopView, ShopViewAll, ShopDetailView, ProductCommentView, SearchResultsView

app_name = 'products'
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('shop/', ShopViewAll.as_view(), name='shop'),
    path('shop/<uuid:uuid>/', ShopView.as_view(), name='shop'),
    path('product/<slug:slug>/<uuid:uuidd>/', ShopDetailView.as_view(), name='shop_detail'),
    path('comment/<uuid:uuid>/', ProductCommentView.as_view(), name='comment_create'),
    path('search/', SearchResultsView.as_view(), name='search'),
    
]
