from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from base.models import Product
from base.serializers import ProductSerializer

from rest_framework import status

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

@api_view(['GET'])
def getProductByCategory(request, category): 
    products = Product.objects.filter(category=category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

