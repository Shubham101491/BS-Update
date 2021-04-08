from django.db import models
from kitchen.models import Kitchen_base
from django.contrib.auth.models import User, auth
import datetime



class Order(models.Model):
    product = models.ForeignKey(Kitchen_base, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=300, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')
    zipcode = models.CharField(max_length=10, default='')
    phone = models.CharField(max_length=10, default='')
    date = models.DateField(default=datetime.datetime.now)

    def placeOrder(self):
        self.save()
        
    # def __str__(self):
    #     return str(self.customer)
