from django.contrib import admin
from .models import Product, ProductImage, ProductVideo, Category, ProductCategory,DiscountCode

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # تعداد فرم‌های اضافی برای اضافه کردن عکس

class ProductVideoInline(admin.TabularInline):
    model = ProductVideo
    extra = 1  # تعداد فرم‌های اضافی برای اضافه کردن ویدئو

class ProductCategoryInline(admin.TabularInline):
    model = ProductCategory
    extra = 1  # امکان انتخاب دسته‌بندی هنگام اضافه کردن محصول

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'is_available', 'get_categories', 'created_at', 'updated_at')  # نمایش دسته‌بندی‌ها
    search_fields = ('name',)  # قابلیت جستجو بر اساس نام محصول
    list_filter = ('is_available', 'categories')  # فیلتر بر اساس موجود بودن و دسته‌بندی
    inlines = [ProductImageInline, ProductVideoInline, ProductCategoryInline]  # نمایش اینلاین دسته‌بندی، عکس و ویدئو

    def get_categories(self, obj):
        """ تابع برای نمایش دسته‌بندی‌های محصول در لیست ادمین """
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = "دسته‌بندی‌ها"  # عنوان ستون در پنل مدیریت

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'caption', 'created_at', 'image_preview')  # نمایش محصول و توضیحات عکس در پنل ادمین

    def image_preview(self, obj):
        """ نمایش پیش‌نمایش تصویر در پنل ادمین """
        return f'<img src="{obj.image.url}" width="100" height="100" />'
    image_preview.allow_tags = True
    image_preview.short_description = "پیش‌نمایش تصویر"

class ProductVideoAdmin(admin.ModelAdmin):
    list_display = ('product', 'caption', 'created_at', 'video_preview')  # نمایش محصول و توضیحات ویدئو در پنل ادمین

    def video_preview(self, obj):
        """ نمایش پیش‌نمایش ویدئو در پنل ادمین """
        return f'<video width="100" height="100" controls><source src="{obj.video.url}" type="video/mp4"></video>'
    video_preview.allow_tags = True
    video_preview.short_description = "پیش‌نمایش ویدئو"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # نمایش نام و توضیحات دسته‌بندی
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percentage', 'valid_from', 'valid_to', 'is_active', 'apply_to_all')  # نمایش اطلاعات در لیست ادمین
    search_fields = ('code',)  # امکان جستجو بر اساس کد تخفیف
    list_filter = ('is_active', 'apply_to_all')  # امکان فیلتر کردن بر اساس وضعیت و اعمال روی همه
    filter_horizontal = ('products', 'categories')  # نمایش انتخاب چندتایی محصولات و دسته‌بندی‌ها

admin.site.register(DiscountCode, DiscountCodeAdmin)  # ثبت مدل در پنل مدیریت

# ثبت مدل‌ها در پنل ادمین
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductVideo, ProductVideoAdmin)
admin.site.register(Category, CategoryAdmin)
