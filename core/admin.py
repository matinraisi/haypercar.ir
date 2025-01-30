from django.contrib import admin
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




