from django.db import models
from django.db.models.base import Model

from accounts.models import AddProducts, Customer

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 
    
    @property
    def product_count(self):
        ordercount=Order.objects.count()
        return ordercount
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

    
class OrderItem(models.Model):
    product  =models.ForeignKey(AddProducts,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True)
    data_added = models.DateTimeField(auto_now_add=True)

    def total_Prod(self):
        return self.product.count()
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

