from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Cart, CartItem

# تابع افزودن محصول به سبد خرید
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # دریافت محصول از دیتابیس

    # اگر کاربر لاگین باشد، یک سبد خرید برای او ایجاد یا دریافت می‌شود
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart, created = Cart.objects.get_or_create(user=None)  # برای کاربران مهمان

    # بررسی اینکه آیا این محصول از قبل در سبد خرید وجود دارد یا خیر
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1  # اگر محصول از قبل در سبد وجود داشت، تعداد آن افزایش می‌یابد
        cart_item.save()

    return redirect('cart_detail')  # انتقال به صفحه جزئیات سبد خرید

# تابع نمایش سبد خرید
def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first() if request.user.is_authenticated else None
    return render(request, 'cart/cart_detail.html', {'cart': cart})

# تابع حذف محصول از سبد خرید
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)  # دریافت آیتم موردنظر
    cart_item.delete()  # حذف آیتم از سبد خرید
    return redirect('cart_detail')  # انتقال به صفحه جزئیات سبد خرید
