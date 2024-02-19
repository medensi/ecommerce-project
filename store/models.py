from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
   user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
   name = models.CharField(max_length=200, null=True)
   email = models.CharField(max_length=200, null=True)

   def __str__(self) -> str:
      return self.name

class Product(models.Model):
   name = models.CharField(max_length=200, null=True)
   price = models.FloatField()
   digital = models.BooleanField(default=False, null=True, blank=False)
   #image

   def __str__(self) -> str:
      return self.name
   
class Order(models.Model):
   customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True) #we set the relationship to class Customer, if customer gets deleted we dont delete their orders (null instead of cascade), cascade deletes everything
   date_ordered = models.DateTimeField(auto_now_add=True)
   complete = models.BooleanField(default=False, null=True, blank=False)
   transaction_id = models.CharField(max_length=200, null=True)

   def __str__(self) -> str:
      return str(self.id)


class OrderItem(models.Model):
   product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True) #order is related to Product
   order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True) #child of Order 
   quantity = models.IntegerField(default=0, null=True, blank=True)
   date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
   customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True) #if order gets deleted, we still have shipping address of the customer
   order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
   address = models.CharField(max_length=200, null=True)
   city = models.CharField(max_length=200, null=True)
   state = models.CharField(max_length=200, null=True)
   zipcode = models.CharField(max_length=200, null=True)
   date_added = models.DateTimeField(auto_now_add=True)

   def __str__(self) -> str:
      return self.address