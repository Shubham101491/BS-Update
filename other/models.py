from django.db import models


class Offer(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class special_offer(models.Model):
    product = models.ForeignKey(Offer,on_delete=models.CASCADE,default=1)
    item = models.CharField(max_length=50)
    image = models.ImageField(upload_to='kitchen/')
    price = models.CharField(max_length=20)
    discount_price = models.CharField(max_length=10)
    detail = models.CharField(max_length=100)
    def __str__(self):
        return str(self.item)

