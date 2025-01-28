<<<<<<< HEAD
# products/admin.py

from django.contrib import admin
from .models import Product, ProductImage, ProductVideo

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # تعداد فرم‌های اضافی برای اضافه کردن عکس

class ProductVideoInline(admin.TabularInline):
    model = ProductVideo
    extra = 1  # تعداد فرم‌های اضافی برای اضافه کردن ویدئو

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'is_available', 'created_at', 'updated_at')  # ستون‌هایی که در لیست محصولات نمایش داده می‌شود
    search_fields = ('name',)  # قابلیت جستجو بر اساس نام محصول
    list_filter = ('is_available',)  # فیلتر بر اساس موجود بودن محصول
    inlines = [ProductImageInline, ProductVideoInline]  # نمایش عکس‌ها و ویدئوها به صورت Inline

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'caption', 'created_at')  # نمایش محصول و توضیحات عکس در پنل ادمین

class ProductVideoAdmin(admin.ModelAdmin):
    list_display = ('product', 'caption', 'created_at')  # نمایش محصول و توضیحات ویدئو در پنل ادمین

# ثبت مدل‌ها در پنل ادمین
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductVideo, ProductVideoAdmin)
=======
from django.contrib import admin

# Register your models here.
>>>>>>> be8b472dbf63522465228c8873ac44da95befb52
