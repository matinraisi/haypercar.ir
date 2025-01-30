from django import forms
from .models import Product, ProductImage, ProductVideo,DiscountCode

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'is_available', 'categories']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'categories': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'name': 'نام محصول',
            'price': 'قیمت',
            'stock': 'موجودی',
            'description': 'توضیحات',
            'categories': 'دسته‌بندی‌ها',
            'is_available': 'وضعیت موجودی',
        }

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image', 'caption']

class ProductVideoForm(forms.ModelForm):
    class Meta:
        model = ProductVideo
        fields = ['video', 'caption']

class DiscountCodeForm(forms.ModelForm):
    class Meta:
        model = DiscountCode
        fields = ['code', 'discount_percentage', 'valid_from', 'valid_to', 'is_active', 'products', 'categories', 'apply_to_all']
        widgets = {
            'valid_from': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # ویجت انتخاب تاریخ و زمان
            'valid_to': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'code': 'کد تخفیف',
            'discount_percentage': 'درصد تخفیف',
            'valid_from': 'تاریخ شروع',
            'valid_to': 'تاریخ پایان',
            'is_active': 'فعال',
            'products': 'محصولات',
            'categories': 'دسته‌بندی‌ها',
            'apply_to_all': 'اعمال روی همه محصولات',
        }
