from django.contrib import admin
from .models import User,Category,Product,Size,Storage,Basket,Favorite,Order,OrderItems

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Storage)
admin.site.register(Basket)
admin.site.register(Favorite)
admin.site.register(Order)
admin.site.register(OrderItems)