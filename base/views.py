from django.shortcuts import render
from django.http import JsonResponse
from .products import products

# Create your views here.

# first view will tell us what routes we have and how our API is going to look
def getRoutes(request):
    #routes for our products
    routes = [
        '/api/products/',
        '/api/products/create',
        '/api/products/upload',
        '/api/products/<id>',
        '/api/products/<delete>/<id>/',
         '/api/products/<update>/<id>'
    ]
    return JsonResponse(routes, safe=False)

#now we need to configure our urls to know when to trigger this view, becuase we're going to have multiple views. We connect our view to urls in urls.py file


# creating another view, later on we'll actually query the db and get back real products
def getProducts(request):
    return JsonResponse(products, safe=False)