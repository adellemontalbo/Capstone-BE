from django.db import models
from django.contrib.auth.models import User

#models.Model turn our class into a model
# one to many relationship = users to products
# we don't want to delete the child elements if the parent element ever gets deleted (i.e. if user is deleted)
# null = False, ok to put product in db without user
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    # image = 
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
  
