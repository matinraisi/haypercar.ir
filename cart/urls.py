from django.urls import path
from .views import add_to_cart, cart_detail, remove_from_cart

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),  # مسیر افزودن محصول
    path('', cart_detail, name='cart_detail'),  # مسیر نمایش سبد خرید
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),  # مسیر حذف محصول
]
