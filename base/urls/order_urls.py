from django.urls import path, include
from base.views import order_views as views


urlpatterns = [

path('add/', views.addOrderItems, name='orders-add'), 
path('<str:id>/', views.getOrderById, name='user-order'), 
path('<str:id>/pay', views.updateOrderToPaid, name='paid'), 
]