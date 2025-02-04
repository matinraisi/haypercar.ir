from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'core/home.html')

def shopping_cart(request):
    return render(request , 'core/shopping_cart.html')