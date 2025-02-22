from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shopping_cart', views.shopping_cart, name='shopping_cart'),
    path('account_settlement', views.account_settlement, name='account_settlement'),
    path('Product_details/<int:pk>', views.Product_details, name='Product_details'),
    path('account_dashboard', views.account_dashboard, name='account_dashboard'),
    path('account_profile', views.account_profile, name='account_profile'),
    path('account_orders', views.account_orders, name='account_orders'),
    path('account_order_details', views.account_order_details, name='account_order_details'),
    path('account_addresses', views.account_addresses, name='account_addresses'),
    path('account_edit_address', views.account_edit_address, name='account_edit_address'),
    path('account_password', views.account_password, name='account_password'),
    path('shop', views.shop, name='shop'),
    path('comments/', views.comment_list, name='comment_list'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('respond/<int:comment_id>/', views.respond_to_comment, name='respond_to_comment'),
<<<<<<< HEAD


=======
    
>>>>>>> 84ae610de1e1aedadfc2d852d5c465640ed4ac29
]
