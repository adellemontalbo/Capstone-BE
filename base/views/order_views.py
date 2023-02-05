from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from base.models import Product, Order, OrderItem, ShippingAddress
from base.serializers import ProductSerializer, OrderSerializer

from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user = request.user
    data = request.data
    orderItems = data['orderItems']

    if orderItems and len(orderItems) == 0:
        return Response({'detail': 'There are no items in order'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        order = Order.objects.create(
            user=user,
            paymentMethod=data['paymentMethod'],
            taxPrice=data['taxPrice'],
            shippingPrice=data['shippingPrice'],
            totalPrice=data['totalPrice']
        )

        shipping = ShippingAddress.objects.create(
            order=order,
            address=data['shippingAddress']['address'],
            city=data['shippingAddress']['city'],
            postalCode=data['shippingAddress']['postalCode'],
            country=data['shippingAddress']['country'],
        )

        for el in orderItems:
            product = Product.objects.get(id=el['product'])
            item = OrderItem.objects.create(
                product = product,
                order = order,
                name = product.name,
                qty = el['qty'],
                price = el['price'],
                image = product.image.url
            )

            product.countInStock -= item.qty
            product.save()
    
        serializer = OrderSerializer(order, many=False)

        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getOrderById(request, id):

    user = request.user

    try:

        order = Order.objects.get(id=id)
        if user.is_staff or order.user == user:
            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)
        else:
            Response({
                'detail': 'Not authorized'
            }, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'detail': 'This order does not exist'}, status=status.HTTP_400_BAD_REQUEST)
