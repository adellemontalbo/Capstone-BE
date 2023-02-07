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

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getOrderById(request, id):

    order = Order.objects.get(id=id)
    # user = request.user
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)

    #I had an error, I was making a post instead of a get request. Auth still not working

    # try:

    #     order = Order.objects.get(id=id)
    #     user = request.user
    #     if user.is_staff or order.user == user:
    #         serializer = OrderSerializer(order, many=False)
    #         return Response(serializer.data)
    #     else:
    #         return Response({
    #             'detail': 'Not authorized'
    #         }, status=status.HTTP_400_BAD_REQUEST)
    # except:
    #     return Response({'detail': 'This order does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateOrderToPaid(request, id):
    order =Order.objects.get(id=id)
    order.isPaid = True
    order.save()
    return Response('Order paid for')
   
