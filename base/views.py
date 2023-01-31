from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['username'] = self.user.username
        data['email'] = self.user.email

        return data
    

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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



