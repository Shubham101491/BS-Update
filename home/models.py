from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.EmailField(max_length=50)


class Home(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Staples(models.Model):
    product = models.ForeignKey(Home, on_delete=models.CASCADE, default=1)
    item = models.CharField(max_length=50)
    image = models.ImageField(upload_to='kitchen/')
    price = models.CharField(max_length=20)
    discount_price = models.CharField(max_length=10)
    detail = models.CharField(max_length=100)
    def __str__(self):
        return str(self.item)


class Snacks(models.Model):
    product = models.ForeignKey(Home, on_delete=models.CASCADE, default=2)
    item = models.CharField(max_length=50)
    image = models.ImageField(upload_to='kitchen/')
    price = models.CharField(max_length=20)
    discount_price = models.CharField(max_length=10)
    detail = models.CharField(max_length=100)
    def __str__(self):
        return str(self.item)


class Fruits_Vegetables(models.Model):
    product = models.ForeignKey(Home, on_delete=models.CASCADE, default=2)
    item = models.CharField(max_length=50)
    image = models.ImageField(upload_to='kitchen/')
    price = models.CharField(max_length=20)
    discount_price = models.CharField(max_length=10)
    detail = models.CharField(max_length=100)
    def __str__(self):
        return str(self.item)


class Breakfast_Cereal(models.Model):
    product = models.ForeignKey(Home, on_delete=models.CASCADE, default=2)
    item = models.CharField(max_length=50)
    image = models.ImageField(upload_to='kitchen/')
    price = models.CharField(max_length=20)
    discount_price = models.CharField(max_length=10)
    detail = models.CharField(max_length=100)
    def __str__(self):
        return str(self.item)