from django.db import models

class Category1(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Kitchen_base(models.Model):
    product = models.ForeignKey(Category1,on_delete=models.CASCADE,default=1)
    item = models.CharField(max_length=50)
    image = models.ImageField(upload_to='kitchen/')
    price = models.CharField(max_length=20)
    discount_price = models.CharField(max_length=10)
    detail = models.CharField(max_length=100)

    def __str__(self):
        return str(self.item)

class popular1(models.Model):
    product = models.ForeignKey(Category1,on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to='kitchen/popular/')
    item = models.CharField(max_length=50)
    caption = models.CharField(max_length=20)

    def __str__(self):
        return str(self.item)

class popular2(models.Model):
    product = models.ForeignKey(Category1,on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to='kitchen/popular/')
    item = models.CharField(max_length=50)
    caption = models.CharField(max_length=20)

    def __str__(self):
        return str(self.item)

class popular3(models.Model):
    product = models.ForeignKey(Category1,on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to='kitchen/popular/')
    item = models.CharField(max_length=50)
    caption = models.CharField(max_length=20)

    def __str__(self):
        return str(self.item)
