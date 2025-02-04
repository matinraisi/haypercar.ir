from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('comments/', views.comment_list, name='comment_list'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('respond/<int:comment_id>/', views.respond_to_comment, name='respond_to_comment'),

]
