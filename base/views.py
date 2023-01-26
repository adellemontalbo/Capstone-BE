from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import products

# first view will tell us what routes we have and how our API is going to look
@api_view(['GET']) # put methods we allow here
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
    return Response(routes)

# later on we'll actually query the db and get back real products
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

