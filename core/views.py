from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm

# ویوی صفحه اصلی
def home(request):
    return render(request, 'core/home.html')

# ویوی نمایش لیست کامنت‌ها
def comment_list(request):
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'core/comment_list.html', {'comments': comments})

# ویوی افزودن کامنت جدید (فقط برای کاربران واردشده)
@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('comment_list')
    else:
        form = CommentForm()
    return render(request, 'core/add_comment.html', {'form': form})

# ویوی پاسخ به کامنت‌ها (فقط برای ادمین‌ها)
@login_required
def respond_to_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # فقط ادمین‌ها می‌توانند پاسخ دهند
    if request.user.is_staff:
        if request.method == 'POST':
            response = request.POST.get('response')
            comment.admin_response = response
            comment.save()
            return redirect('comment_list')
        return render(request, 'core/respond_to_comment.html', {'comment': comment})
    else:
        return redirect('comment_list')

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'core/home.html')
