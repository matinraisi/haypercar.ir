from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from django_jalali.db.models import jDateTimeField  # اضافه کردن تاریخ جلالی
from django_resized import ResizedImageField  # تغییر اندازه خودکار تصویر
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="نام دسته‌بندی")  # نام دسته‌بندی محصول
    description = models.TextField(blank=True, verbose_name="توضیحات دسته‌بندی")  # توضیحات مربوط به دسته‌بندی

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)  # نام محصول
    description = models.TextField()  # توضیحات محصول
    price = models.DecimalField(max_digits=10, decimal_places=0)  # قیمت محصول
    stock = models.PositiveIntegerField(default=1)  # تعداد موجودی محصول
    is_available = models.BooleanField(default=True)  # وضعیت موجودی محصول
    categories = models.ManyToManyField(Category, related_name='products', through='ProductCategory')  # ارتباط محصول با دسته‌بندی‌ها
    created_at = jDateTimeField(auto_now_add=True)  # تاریخ ایجاد محصول (جلالی)
    updated_at = jDateTimeField(auto_now=True)  # تاریخ به‌روزرسانی محصول (جلالی)
   
    def __str__(self):
        return self.name

    def reduce_stock(self, quantity):
        """ کاهش موجودی پس از خرید """
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()

    def clean(self):
        """ اعتبارسنجی مقدار موجودی """
        if self.stock is None or self.stock < 0:
            raise ValidationError("موجودی نمی‌تواند منفی باشد.")
        self.is_available = self.stock > 0

    def save(self, *args, **kwargs):
        """ انجام اعتبارسنجی قبل از ذخیره سازی """
        self.clean()
        super().save(*args, **kwargs)

class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # ارتباط با محصول
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # ارتباط با دسته‌بندی
    
    class Meta:
        unique_together = ('product', 'category')  # جلوگیری از تکرار یک دسته‌بندی برای یک محصول خاص
    
    def __str__(self):
        return f"{self.product.name} -> {self.category.name}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)  # ارتباط با محصول
    image = ResizedImageField(
        size=[500, 500],  # تغییر اندازه به 500×500 پیکسل
        quality=75,  # فشرده‌سازی برای کاهش حجم
        crop=['middle', 'center'],  # برش تصویر از وسط
        force_format="WEBP",  # ذخیره به‌صورت WEBP برای کاهش حجم
        upload_to='products/images/'
    )
    caption = models.CharField(max_length=255, blank=True)  # توضیحات تصویر
    created_at = jDateTimeField(auto_now_add=True)  # تاریخ ایجاد تصویر (جلالی)

    def __str__(self):
        return f"Image for {self.product.name}"

class ProductVideo(models.Model):
    product = models.ForeignKey(Product, related_name='videos', on_delete=models.CASCADE)  # ارتباط با محصول
    video = models.FileField(upload_to='products/videos/')  # ویدیو محصول
    caption = models.CharField(max_length=255, blank=True)  # توضیحات ویدیو
    created_at = jDateTimeField(auto_now_add=True)  # تاریخ ایجاد ویدیو (جلالی)
    # حذف تصویر بندانگشتی و تغییر اندازه ویدیو با کتابخانه‌ای مانند ffmpeg انجام می‌شود

    def __str__(self):
        return f"Video for {self.product.name}"
class DiscountCode(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="کد تخفیف")  # کد یکتای تخفیف
    discount_percentage = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name="درصد تخفیف"
    )  # درصد تخفیف بین 1 تا 100
    valid_from = jDateTimeField(verbose_name="شروع اعتبار")  # زمان شروع اعتبار کد تخفیف
    valid_to = jDateTimeField(verbose_name="پایان اعتبار")  # زمان پایان اعتبار کد تخفیف
    is_active = models.BooleanField(default=True, verbose_name="فعال")  # وضعیت فعال بودن کد تخفیف
    
    # انتخاب اینکه کد تخفیف روی چه چیزی اعمال شود
    products = models.ManyToManyField('Product', blank=True, related_name='discounts', verbose_name="محصولات")  # اعمال روی محصولات خاص
    categories = models.ManyToManyField('Category', blank=True, related_name='discounts', verbose_name="دسته‌بندی‌ها")  # اعمال روی دسته‌بندی‌های خاص
    apply_to_all = models.BooleanField(default=False, verbose_name="اعمال روی همه محصولات")  # امکان اعمال روی همه محصولات
    
    def __str__(self):
        return self.code
    
    def is_valid(self):
        """ بررسی معتبر بودن کد تخفیف """
        from django.utils.timezone import now
        return self.is_active and self.valid_from <= now() <= self.valid_to
