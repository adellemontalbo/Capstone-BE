from django.urls import path, include
from . import views

#list of urls (paths)
#we need to tell our django project (in backend), whenever we enter the homepage, send the traffic to our first path (left blank because it's the home url)
# whenever we type in said route we should trigger the appropriate view
urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('products/', views.getProducts, name="products"),
    path('products/<id>', views.getProduct, name="product"),
]