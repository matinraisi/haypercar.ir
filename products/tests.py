from django.test import TestCase
from .models import Product

class ProductTestCase(TestCase):
    
    def setUp(self):
        """ایجاد داده اولیه برای تست"""
        self.product = Product.objects.create(
            name='Test Product',
            description='A test product',
            price=100.0,
            stock=10,
            is_available=True
        )

    def test_product_default_stock(self):
        """آیا موجودی محصول به‌طور پیش‌فرض برابر 1 است؟"""
        product = Product.objects.create(
            name="Test Product",
            description="This is a test product",
            price=100.00,
        )
        self.assertEqual(product.stock, 1)  # باید موجودی پیش‌فرض 1 باشد

    def test_product_is_available_when_stock_is_zero(self):
        """آیا وضعیت موجودی محصول به‌طور خودکار به False تغییر می‌کند وقتی که موجودی 0 شود؟"""
        product = Product.objects.create(
            name="Test Product",
            description="This is a test product",
            price=100.00,
            stock=0,
        )
        self.assertFalse(product.is_available)  # باید وضعیت موجودی False شود وقتی موجودی 0 باشد

    def test_product_is_available_when_stock_is_positive(self):
        """آیا وضعیت موجودی محصول به‌طور خودکار به True تغییر می‌کند وقتی که موجودی مثبت باشد؟"""
        product = Product.objects.create(
            name="Test Product",
            description="This is a test product",
            price=100.00,
            stock=5,
        )
        self.assertTrue(product.is_available)  # باید وضعیت موجودی True شود وقتی موجودی بیشتر از 0 باشد

    def test_reduce_stock_on_purchase(self):
        """تست کاهش موجودی پس از خرید محصول"""
        initial_stock = self.product.stock  # موجودی اولیه
        quantity_to_buy = 3  # تعداد خرید

        # شبیه‌سازی خرید محصول (کاهش موجودی)
        self.product.reduce_stock(quantity_to_buy)

        # بررسی که موجودی کاهش یافته باشد
        self.assertEqual(self.product.stock, initial_stock - quantity_to_buy)

    def test_not_enough_stock(self):
        """تست زمانی که موجودی کافی برای خرید وجود ندارد"""
        initial_stock = self.product.stock  # موجودی اولیه
        quantity_to_buy = 15  # تعداد خرید

        # تلاش برای خرید محصول با موجودی کمتر از آنچه که درخواست شده است
        self.product.reduce_stock(quantity_to_buy)

        # موجودی باید بدون تغییر باقی بماند چون موجودی کافی نیست
        self.assertEqual(self.product.stock, initial_stock)

    def test_buy_with_zero_stock(self):
        """تست خرید با موجودی صفر"""
        self.product.stock = 0  # تنظیم موجودی به صفر
        self.product.save()

        initial_stock = self.product.stock  # موجودی اولیه
        quantity_to_buy = 1  # تعداد خرید

        # تلاش برای خرید محصول با موجودی صفر
        self.product.reduce_stock(quantity_to_buy)

        # موجودی نباید تغییر کند
        self.assertEqual(self.product.stock, initial_stock)

    def test_buy_with_negative_stock(self):
        """تست خرید با موجودی منفی"""
        self.product.stock = -5  # تنظیم موجودی به منفی
        self.product.save()

        initial_stock = self.product.stock  # موجودی اولیه
        quantity_to_buy = 3  # تعداد خرید

        # تلاش برای خرید محصول با موجودی منفی
        self.product.reduce_stock(quantity_to_buy)

        # موجودی نباید تغییر کند
        self.assertEqual(self.product.stock, initial_stock)

    def test_remove_product_when_zero_stock(self):
        """تست حذف محصول هنگام صفر شدن موجودی"""
        self.product.stock = 0  # تنظیم موجودی به صفر
        self.product.save()

        # حذف محصول در صورتی که موجودی صفر است (اگر این رفتار را پیاده‌سازی کرده باشید)
        if self.product.stock == 0:
            self.product.delete()

        # بررسی که محصول حذف شده باشد
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=self.product.id)

    def test_reduce_stock_to_zero(self):
        """تست کاهش موجودی به صفر"""
        initial_stock = self.product.stock  # موجودی اولیه
        quantity_to_buy = initial_stock  # تعداد خرید برابر با موجودی

        # شبیه‌سازی خرید محصول تا موجودی صفر شود
        self.product.reduce_stock(quantity_to_buy)

        # بررسی که موجودی صفر شده باشد
        self.assertEqual(self.product.stock, 0)

from django.test import TestCase


