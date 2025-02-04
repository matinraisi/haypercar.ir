from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'core/home.html')

def shopping_cart(request):
    return render(request , 'core/shopping_cart.html')

def account_settlement(request):
    return render(request , 'core/account_settlement.html')

def Product_details(request):
    return render(request , 'core/Product_details.html')

def account_dashboard(request):
    return render(request , 'core/account-dashboard.html')
def account_profile(request):
    return render(request , 'core/account-profile.html')
def account_orders(request):
    return render(request , 'core/account-orders.html')

def account_order_details(request):
    return render(request , 'core/account-order-details.html')

def account_addresses(request):
    return render(request , 'core/account-addresses.html')
def account_edit_address(request):
    return render(request , 'core/account-edit-address.html')
def account_password(request):
    return render(request , 'core/account-password.html')


