from .models import Category
from app.order.models import Wishlist, ShopCart, OrderInfo

def get_categories(request):
    all_price = 0
    categories  = Category.objects.filter(is_active=True, parent=None)
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user = request.user)
        shopcart = ShopCart.objects.filter(user = request.user)
        order_item = OrderInfo.objects.filter(user = request.user, status='Completed')
        
        
        for i in shopcart:
            
                all_price += int(i.quenty*i.product_price)
                
                
            
    else:
        wishlist = []
        shopcart = []
        order_item = []
    context = {
        'categories': categories,
        'wishlist' : wishlist,
        'shopcart' : shopcart,
        'all_price' : all_price,
        'order_item' : order_item
    }
    return  context