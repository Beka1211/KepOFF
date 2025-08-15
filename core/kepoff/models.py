from django.db import models
from user.models import MyUserManager,MyUser

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brands/logos/')

    def __str__(self):
        return self.title


class Size(models.Model):
    size_name = models.CharField(max_length=10)


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products")
    old_price = models.DecimalField(max_digits=15, decimal_places=2)
    new_price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    brands = models.ManyToManyField(Brand, related_name="products")

    def __str__(self):
        return self.title


class Storage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product} [{self.size}] {self.quantity}"


class Favorite(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Basket(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    storage = models.ManyToManyField(Storage)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
