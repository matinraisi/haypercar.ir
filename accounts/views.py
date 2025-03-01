# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import logout
from .models import CustomUser
from django.db import IntegrityError

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()  # ذخیره کاربر
                phone_number = form.cleaned_data.get('phone_number')
                password = form.cleaned_data.get('password1')

                # احراز هویت کاربر
                user = authenticate(username=phone_number, password=password)
                if user is not None:
                    login(request, user)  # ورود کاربر
                    return redirect('home')
            except IntegrityError:
                form.add_error('phone_number', 'این شماره تلفن قبلاً استفاده شده است.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            # فرم نادرست است و خطاها را ارسال می‌کنیم
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
