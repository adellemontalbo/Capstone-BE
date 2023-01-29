from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product

#convention is write model name followed by serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        #here is what we want to render out, we can list them out, in out case we want all 
        fields = '__all__'
