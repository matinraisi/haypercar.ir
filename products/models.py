<<<<<<< HEAD
from django.core.exceptions import ValidationError
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=1)  # مقدار پیش‌فرض 1
    is_available = models.BooleanField(default=True)  # وضعیت موجودی به‌صورت پیش‌فرض موجود
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
=======
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام محصول")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت")
    part_number = models.CharField(max_length=100, unique=True, verbose_name="شماره قطعه")
    stock = models.PositiveIntegerField(default=0, verbose_name="موجودی")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    image = models.ImageField(upload_to='product_images/', blank=True, verbose_name="تصویر محصول")
    brand = models.CharField(max_length=100, verbose_name="برند")
    categories = models.ManyToManyField('Category', related_name='products', verbose_name="دسته‌بندی‌ها")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
>>>>>>> be8b472dbf63522465228c8873ac44da95befb52

    def __str__(self):
        return self.name

<<<<<<< HEAD
    def reduce_stock(self, quantity):
        """کاهش تعداد موجودی محصول پس از خرید"""
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()

    def clean(self):
        """اعتبارسنجی برای جلوگیری از مقدار منفی موجودی"""
        if self.stock is None or self.stock < 0:
            raise ValidationError("موجودی نمی‌تواند منفی باشد.")
        # تعیین وضعیت موجودی به صورت خودکار
        if self.stock <= 0:
            self.is_available = False
        else:
            self.is_available = True

    def save(self, *args, **kwargs):
        """اعتبارسنجی پیش از ذخیره کردن و تنظیم وضعیت موجودی"""
        self.clean()
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)  # ارتباط با محصول
    image = models.ImageField(upload_to='products/images/')  # عکس محصول
    caption = models.CharField(max_length=255, blank=True)  # توضیحات عکس
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد عکس

    def __str__(self):
        return f"Image for {self.product.name}"

class ProductVideo(models.Model):
    product = models.ForeignKey(Product, related_name='videos', on_delete=models.CASCADE)  # ارتباط با محصول
    video = models.FileField(upload_to='products/videos/')  # ویدئو محصول
    caption = models.CharField(max_length=255, blank=True)  # توضیحات ویدئو
    created_at = models.DateTimeField(auto_now_add=True)  # تاریخ ایجاد ویدئو

    def __str__(self):
        return f"Video for {self.product.name}"
=======
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="نام دسته‌بندی")
    description = models.TextField(blank=True, verbose_name="توضیحات دسته‌بندی")

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # استفاده از مدل کاربر سفارشی
        on_delete=models.CASCADE
    )
    # سایر فیلدهای مدل
>>>>>>> be8b472dbf63522465228c8873ac44da95befb52
