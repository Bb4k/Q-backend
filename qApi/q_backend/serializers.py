from . import models
from rest_framework import serializers


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class ShopProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShopProduct
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
