from django.db import models
from django.contrib.auth.models import User

# models.Model turn our class into a model
# one to many relationship = users to products
# we don't want to delete the child elements if the parent element ever gets deleted (i.e. if user is deleted)
# null = False, ok to put product in db without user

class Product(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name
  

class Order(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #should we have this default to CC?
    paymentMethod = models.CharField(max_length=100, null=True, blank=True)
    taxPrice = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.BooleanField(default=False)

    def __str__(self):
        return str(self.createdAt)
    
class OrderItem(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    order = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class ShippingAddress(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.address)