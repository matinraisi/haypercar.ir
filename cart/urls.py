from django.urls import path
from .views import add_to_cart, cart_detail, update_cart, remove_from_cart, clear_cart

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),  # افزودن محصول
    path('', cart_detail, name='cart_detail'),  # نمایش سبد خرید
    path('update/<int:item_id>/<str:action>/', update_cart, name='update_cart'),  # افزایش یا کاهش تعداد
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),  # حذف یک محصول
    path('clear/', clear_cart, name='clear_cart'),  # خالی کردن کل سبد خرید
]
