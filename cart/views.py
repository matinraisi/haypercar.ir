from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CartItem
from products.models import Product
from django.http import HttpResponse

# این ویو سبد خرید را نمایش می‌دهد
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    
    # محاسبه مجموع قیمت‌ها
    cart_total = sum(item.product.price * item.quantity for item in cart_items)
    shipping_fee = 10.0  # می‌توانید این را به دلخواه تنظیم کنید
    tax = cart_total * 0.1  # مالیات به طور فرضی 10 درصد
    grand_total = cart_total + shipping_fee + tax
    
    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'shipping_fee': shipping_fee,
        'tax': tax,
        'grand_total': grand_total,
    }
    
    return render(request, 'cart/shopping_cart.html', context)

# این ویو برای اضافه کردن محصول به سبد خرید است
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    quantity = int(request.POST.get('quantity', 1))  # دریافت مقدار تعداد از فرم
    
    # بررسی اینکه آیا محصول قبلاً در سبد خرید هست یا خیر
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, 
        product=product,
        is_active=True
    )
    
    if not created:
        cart_item.quantity += quantity  # اگر محصول قبلاً هست تعداد آن را افزایش می‌دهیم
        cart_item.save()

    messages.success(request, f"{product.name} به سبد خرید شما اضافه شد.")
    return redirect('view_cart')

# این ویو برای حذف محصول از سبد خرید است
def remove_from_cart(request, product_id):
    cart_item = CartItem.objects.get(user=request.user, product_id=product_id, is_active=True)
    cart_item.delete()
    
    messages.success(request, "محصول از سبد خرید شما حذف شد.")
    return redirect('view_cart')

# این ویو برای بروزرسانی تعداد محصول در سبد خرید است
def update_cart(request, product_id):
    cart_item = CartItem.objects.get(user=request.user, product_id=product_id, is_active=True)
    new_quantity = int(request.POST.get('quantity'))
    
    if new_quantity > 0:
        cart_item.quantity = new_quantity
        cart_item.save()
        messages.success(request, "تعداد محصول با موفقیت بروزرسانی شد.")
    else:
        cart_item.delete()
        messages.success(request, "محصول از سبد خرید حذف شد.")

    return redirect('view_cart')
