from django.urls import path
from .views import WithListView, WithListUuidView, WishListDeleteView, ShopCartListView, ShopCartDeleteView, ShopCartDeleteAllView, \
    ShopCartAddOneView, OrderCreateView, OrderCreateOneClikView, OrderVariantView,\
     OrderCreateInfoView, NotificationView, OrderInfoDeleteView

app_name = 'order'
urlpatterns = [
    path('wishlist/<uuid:uuid>/', WithListUuidView.as_view(), name='wishlist_product'),
    path('wishlist/', WithListView.as_view(), name='wishlist'),
    path('wishlist/<uuid:uuid>/delete/', WishListDeleteView.as_view(), name='wishlist_delete'),
    path('shop-cart-list/', ShopCartListView.as_view(), name='shop_cat_list'),
    path('shop-cart/<uuid:uuid>/delete/', ShopCartDeleteView.as_view(), name='shop_cart_delete'),
    path('shop-delete-all/', ShopCartDeleteAllView.as_view(), name='shop_delete_all'),
    path('shop-cart/<uuid:uuid>/', ShopCartAddOneView.as_view(), name='shop_cart_product'),
    path('order-create/', OrderCreateView.as_view(), name='order_create'),
    path('order-create-one-click/<uuid:uuid>/', OrderCreateOneClikView.as_view(), name='order_create_one_click'),
    path('order-create-info/<uuid:uuid>/', OrderCreateInfoView.as_view(), name='order_create_info'),
    path('order-create-variant/<uuid:uuid>/', OrderVariantView.as_view(), name='order_create_variant'),
    path('notification/', NotificationView.as_view(), name='notification'),
    path('order_info_delete/<uuid:uuid>/delete/', OrderInfoDeleteView.as_view(), name='order_info_delete'),


]