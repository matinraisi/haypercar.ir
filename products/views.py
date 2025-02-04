from django.shortcuts import render, redirect
from .models import Product, ProductImage, ProductVideo
from .forms import ProductForm, ProductImageForm, ProductVideoForm
# ایمپورت کلاس‌های لازم برای تعریف ویوهای مبتنی بر کلاس
from django.views.generic import ListView, DetailView
from .models import Product, Category  # ایمپورت مدل‌های Product و Category برای استفاده در ویوها

def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)
        video_form = ProductVideoForm(request.POST, request.FILES)

        if product_form.is_valid():
            product = product_form.save()  # ذخیره محصول
            if 'image' in request.FILES:
                for image in request.FILES.getlist('image'):
                    ProductImage.objects.create(product=product, image=image)  # ذخیره عکس‌ها
            if 'video' in request.FILES:
                for video in request.FILES.getlist('video'):
                    ProductVideo.objects.create(product=product, video=video)  # ذخیره ویدئوها
            return redirect('product_list')  # هدایت به صفحه لیست محصولات
    else:
        product_form = ProductForm()
        image_form = ProductImageForm()
        video_form = ProductVideoForm()

    return render(request, 'products/add_product.html', {'product_form': product_form, 'image_form': image_form, 'video_form': video_form})


# ویوی لیست محصولات
class ProductListView(ListView):
    model = Product  # مشخص کردن مدل مرتبط با این ویو (Product)
    template_name = 'store/product_list.html'  # مشخص کردن قالبی که داده‌ها در آن نمایش داده می‌شوند
    context_object_name = 'products'  # تعیین نام داده‌ای که به قالب ارسال می‌شود (products)

# ویوی جزئیات یک محصول
class ProductDetailView(DetailView):
    model = Product  # مشخص کردن مدل مرتبط (Product)
    template_name = 'store/product_detail.html'  # تعیین قالب نمایش جزئیات یک محصول
    context_object_name = 'product'  # نام داده‌ای که جزئیات محصول را در قالب در دسترس قرار می‌دهد (product)

# ویوی جزئیات یک دسته‌بندی
class CategoryDetailView(DetailView):
    model = Category  # مشخص کردن مدل مرتبط (Category)
    template_name = 'store/category_detail.html'  # تعیین قالب نمایش جزئیات یک دسته‌بندی
    context_object_name = 'category'  # نام داده‌ای که جزئیات دسته‌بندی را در قالب در دسترس قرار می‌دهد (category)
