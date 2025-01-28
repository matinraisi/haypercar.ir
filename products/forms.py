<<<<<<< HEAD
# products/forms.py

from django import forms
from .models import Product, ProductImage, ProductVideo
=======
from django import forms
from .models import Product
>>>>>>> be8b472dbf63522465228c8873ac44da95befb52

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
<<<<<<< HEAD
        fields = ['name', 'description', 'price', 'stock', 'is_available']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image', 'caption']

class ProductVideoForm(forms.ModelForm):
    class Meta:
        model = ProductVideo
        fields = ['video', 'caption']
=======
        fields = ['name', 'price', 'part_number', 'stock', 'description', 'image', 'brand', 'categories']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'categories': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'name': 'نام محصول',
            'price': 'قیمت',
            'part_number': 'شماره قطعه',
            'stock': 'موجودی',
            'description': 'توضیحات',
            'image': 'تصویر محصول',
            'brand': 'برند',
            'categories': 'دسته‌بندی‌ها',
        }
>>>>>>> be8b472dbf63522465228c8873ac44da95befb52
