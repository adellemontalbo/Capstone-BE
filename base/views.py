from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
# from .products import products
from .serializers import ProductSerializer


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

# Get all products
@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    #here it will serialize all our products
    #the many=True is saying we're serializing multiple objects
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

#get one product
@api_view(['GET'])
def getProduct(request, id): 
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)



