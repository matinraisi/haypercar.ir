from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Comment
from .forms import CommentForm

class CommentTests(TestCase):

    def setUp(self):
        # ساخت یک کاربر برای استفاده در تست‌ها
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='password123'
        )
        # URL ویوها
        self.comment_list_url = reverse('comment_list')
        self.add_comment_url = reverse('add_comment')
        # ایجاد یک کامنت برای استفاده در تست‌ها
        self.comment = Comment.objects.create(
            user=self.user,
            content="Test comment"
        )

    # تست مدل Comment
    def test_comment_creation(self):
        comment = Comment.objects.create(
            user=self.user,
            content="This is a test comment"
        )
        self.assertEqual(comment.user.username, 'testuser')
        self.assertEqual(comment.content, "This is a test comment")
        self.assertIsNotNone(comment.created_at)

    # تست ویو comment_list
    def test_comment_list_view(self):
        response = self.client.get(self.comment_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test comment")

    # تست ویو add_comment (برای کاربران وارد شده)
    def test_add_comment_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(self.add_comment_url, {'content': 'Test comment'})
        self.assertEqual(response.status_code, 302)  # redirect to comment list
        comment = Comment.objects.first()
        self.assertEqual(comment.content, 'Test comment')

    # تست ویو add_comment (برای کاربران وارد نشده)
    def test_add_comment_unauthenticated(self):
        response = self.client.post(self.add_comment_url, {'content': 'Test comment'})
        self.assertEqual(response.status_code, 302)  # redirect to login page

    # تست فرم CommentForm
    def test_valid_form(self):
        form_data = {'content': 'This is a valid comment'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'content': ''}  # فیلد خالی
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
