from django.urls import path, include
from . import views

'''
Here we connect our views to our urls

We need to tell our django project (in backend), whenever we enter the homepage, send the traffic to our first path (left blank because it's the home url)

Whenever we type in any of the following paths, we should trigger the appropriate view
'''

# list of urls (paths) - we can name them
urlpatterns = [
    path('users/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', views.getRoutes, name="routes"),
    path('users/profile', views.getUserProfile, name="user-profile"),
    path('users/', views.getUsers, name="users"),
    path('products/', views.getProducts, name="products"),
    path('products/<id>', views.getProduct, name="product"),
]