from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import (User,Category, Brand,
                     Size,Product,Storage,
                     Favorite,Basket,
                     Order, OrderItems)

from .serializers import (
    UserSerializer, CategorySerializer, BrandSerializer,
    SizeSerializer, ProductSerializer, StorageSerializer,
    FavoriteSerializer, BasketSerializer,
    OrderSerializer, OrderItemsSerializer
)


class IndexView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

