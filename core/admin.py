from django.contrib import admin
<<<<<<< HEAD
from .models import Comment

# ثبت مدل Comment در پنل ادمین برای مدیریت نظرات
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # ستون‌هایی که در لیست نمایش داده می‌شوند
    list_display = ('user', 'content', 'created_at', 'updated_at')
    # امکان جستجو بر اساس نام کاربری و محتوای کامنت
    search_fields = ('user__username', 'content')
    # فیلتر بر اساس زمان ایجاد کامنت
    list_filter = ('created_at',)
=======

# Register your models here.
>>>>>>> be8b472dbf63522465228c8873ac44da95befb52
