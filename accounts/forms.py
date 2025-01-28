# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'شماره تلفن'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}))

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['phone_number']  # تخصیص شماره تلفن به username
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'شماره تلفن'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
