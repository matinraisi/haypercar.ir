from django.contrib import admin
from .models import Cart, CartItem

# تنظیمات نمایش آیتم‌های سبد خرید در صفحه ادمین
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1  # تعداد فیلدهای اضافی هنگام ایجاد سبد جدید

# تنظیمات نمایش سبد خرید در پنل ادمین
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')  # نمایش اطلاعات اصلی سبد خرید
    inlines = [CartItemInline]  # نمایش آیتم‌های سبد خرید در داخل سبد خرید

admin.site.register(Cart, CartAdmin)  # ثبت مدل سبد خرید
