from django.db import models
from django.conf import settings
from products.models import Product  

class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
        related_name='cart', null=True, blank=True
    )  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"سبد خرید {self.id} برای {self.user}" if self.user else f"سبد خرید مهمان {self.id}"

    def get_total_price(self):
        
        return sum(item.get_total_price() for item in self.items.all())


# مدل آیتم‌های سبد خرید (محصولاتی که در سبد خرید وجود دارند)
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')  # ارتباط با مدل سبد خرید
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # ارتباط با محصول
    quantity = models.PositiveIntegerField(default=1)  # تعداد محصول در سبد

    def __str__(self):
        return f"{self.quantity} عدد از {self.product.name}"

    def get_total_price(self):
        # محاسبه قیمت کل آیتم
        return self.product.price * self.quantity  # قیمت کل = قیمت واحد * تعداد
