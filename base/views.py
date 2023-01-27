from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import products

# first view will tell us what routes we have and how our API is going to look
@api_view(['GET', 'POST', 'PUT']) # put methods we allow here
def getRoutes(request):
    #routes for our products
    routes = [
        '/api/products/',
         '/api/products/<id>',
        # '/api/products/create',
        # '/api/products/upload',
        # '/api/products/<delete>/<id>/',
        #  '/api/products/<update>/<id>'
    ]
    return Response(routes)

# later on we'll actually query the db and get back real products, right now we just imported our sample products list

'''
REST framework allows you to work with regular function based views. 
It provides a set of simple decorators that wrap your function based views to ensure they receive an instance of Request (rather than the usual Django HttpRequest) and allows them to return a Response (instead of a Django HttpResponse), and allow you to configure how the request is processed.
By default only GET methods will be accepted (you can alter this)
https://www.django-rest-framework.org/api-guide/views/
'''

# Get all products
@api_view(['GET'])
def getProducts(request):
    return Response(products)

#get one product
@api_view(['GET'])
def getProduct(request, id): 
    product = None
    for item in products:
        if item['id'] == id:
            product = item
            break
    return Response(product)



