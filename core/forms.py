from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class AdminResponseForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['admin_response']
