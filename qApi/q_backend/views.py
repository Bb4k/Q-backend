import math

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, HttpResponseNotFound
from django.db.models import Q
import random

from .generateMap import main
from . import models
from . import serializers

ID_NOT_PROVIDED = "ID not provided"
DATA_PROVIDED_IS_NOT_VALID = "Data isn't valid"
ENTITY_NOT_FOUND = "Entity not found"
ENTITY_ADDED_SUCCESSFULLY = "Entity added successfully"
ENTITY_UPDATED_SUCCESSFULLY = "Entity updated successfully"
ENTITY_DELETED_SUCCESSFULLY = "Entity deleted successfully"


class Product:
    def __init__(self, product_id, x, y):
        self.product_id = product_id
        self.x = x
        self.y = y


########################################################################
@api_view(['GET'])
def get_shops(request):
    shops = models.Shop.objects.all()
    serializer = serializers.ShopSerializer(shops, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_products(request):
    shops = models.Product.objects.all()
    serializer = serializers.ProductSerializer(shops, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_shops_products(request):
    shops = models.ShopProduct.objects.all()
    serializer = serializers.ShopProductSerializer(shops, many=True)
    return Response(serializer.data)


########################################################################

@api_view(['POST'])
def post_shop(request):
    data = JSONParser().parse(request)
    shop_serializer = serializers.ShopSerializer(data=data)
    if shop_serializer.is_valid():
        shop_serializer.save()
        return HttpResponse(ENTITY_ADDED_SUCCESSFULLY)
    return HttpResponseNotFound(DATA_PROVIDED_IS_NOT_VALID)


@api_view(['POST'])
def post_product(request):
    data = JSONParser().parse(request)
    product_serializer = serializers.ProductSerializer(data=data)
    if product_serializer.is_valid():
        product_serializer.save()
        return HttpResponse(ENTITY_ADDED_SUCCESSFULLY)
    return HttpResponseNotFound(DATA_PROVIDED_IS_NOT_VALID)


@api_view(['POST'])
def post_shops_product(request):
    data = JSONParser().parse(request)
    shop_product_serializer = serializers.ShopProductSerializer(data=data)
    if shop_product_serializer.is_valid():
        shop_product_serializer.save()
        return HttpResponse(ENTITY_ADDED_SUCCESSFULLY)
    return HttpResponseNotFound(DATA_PROVIDED_IS_NOT_VALID)


########################################################################


@api_view(['GET'])
def get_products_preview(request):

    products = models.Product.objects.all()
    product_serializer = serializers.ProductSerializer(products, many=True)
    products = []
    for product in product_serializer.data:
        all_products_from_shops = models.ShopProduct.objects.filter(product_id=product['id'])
        shops_products_serializer = serializers.ShopProductSerializer(all_products_from_shops, many=True)
        max_price = -1
        min_price = math.inf
        for shops_product in shops_products_serializer.data:
            if shops_product['price'] * shops_product['discount'] > max_price:
                max_price = shops_product['price'] * shops_product['discount']
            if shops_product['price'] * shops_product['discount'] < min_price:
                min_price = shops_product['price'] * shops_product['discount']

        current_product = product
        current_product['range'] = [str(min_price), str(max_price)]
        products.append(current_product)

    return Response(products)


########################################################################

@api_view(['GET'])
def get_product_from_shop(request, shop_id, product_id):
    # print(shop_id, product_id)
    product_from_shop = models.ShopProduct.objects.filter(shop_id=shop_id).filter(product_id=product_id)
    product_from_shop_serializer = serializers.ShopProductSerializer(product_from_shop, many=True)
    # print(product_from_shop_serializer.data)
    price, discount = product_from_shop_serializer.data[0]['price'], product_from_shop_serializer.data[0]['discount']

    product = models.Product.objects.filter(id=product_id)
    product_serializer = serializers.ProductSerializer(product, many=True)
    complete_product = product_serializer.data[0]
    # print(product_serializer.data)
    complete_product['range'] = [str(price)]
    complete_product['discount'] = str(discount)

    return Response(complete_product)


########################################################################
# [[id, quantity], [id, quantity]]
@api_view(['POST'])
def get_basket_prices(request):
    data = JSONParser().parse(request)
    basket_from_shops = []

    shops = models.Shop.objects.all()
    shops_serializer = serializers.ShopSerializer(shops, many=True)

    for shop in shops_serializer.data:
        shop_to_push = dict()
        shop_to_push['logo'] = shop['logo_link']
        shop_to_push['name'] = shop['name']
        shop_to_push['total'] = 0
        for product in data['basket']:
            product_from_shop = models.ShopProduct.objects.filter(shop_id=shop['id']).filter(product_id=product[0])
            product_serializer = serializers.ShopProductSerializer(product_from_shop, many=True)
            if product_serializer.data[0]:
                shop_to_push['total'] += product_serializer.data[0]['price'] * product_serializer.data[0]['discount']

        number = random.randint(0, 2)
        if number == 0:
            shop_to_push['busy'] = [0, 10, 15]
        elif number == 1:
            shop_to_push['busy'] = [1, 30, 45]
        elif number == 2:
            shop_to_push['busy'] = [2, 60, 90]
        basket_from_shops.append(shop_to_push)

    basket_from_shops = sorted(basket_from_shops, key=lambda d: d['total'])
    return Response(basket_from_shops)


########################################################################
# [id, id]
@api_view(['POST'])
def get_map(request, shop_id):
    data = JSONParser().parse(request)
    products = []
    for id in data['products']:
        product_from_shop = models.ShopProduct.objects.filter(shop_id=shop_id).filter(product_id=id)
        product_from_shop_serializer = serializers.ShopProductSerializer(product_from_shop, many=True)
        product = Product(id, product_from_shop_serializer.data[0]['x_coordinate'],
                          product_from_shop_serializer.data[0]['y_coordinate'])
        products.append(product)

    shop = models.Shop.objects.filter(id=shop_id)
    shop_serializer = serializers.ShopSerializer(shop, many=True)
    map = main.generate_map(shop_serializer.data[0]['x_enter'], shop_serializer.data[0]['y_enter'],
                            shop_serializer.data[0]['x_exit'], shop_serializer.data[0]['y_exit'], products)
    # print(map)
    return Response(map)


########################################################################
@api_view(['GET'])
def get_offers(request):
    offers = []
    products_with_discount = models.ShopProduct.objects.filter(~Q(discount=1.0))
    products_with_discount_serializer = serializers.ShopProductSerializer(products_with_discount, many=True)
    for offer in products_with_discount_serializer.data:
        current_offer = dict()
        current_offer['price'] = offer['price']
        current_offer['discount'] = offer['discount']
        current_offer['id'] = offer['product']
        current_offer['shop_id'] = offer['shop']

        product = models.Product.objects.filter(id=offer['product'])
        product_serializer = serializers.ProductSerializer(product, many=True)

        current_offer['name'] = product_serializer.data[0]['name']
        current_offer['image_link'] = product_serializer.data[0]['image_link']

        shop = models.Shop.objects.filter(id=offer['shop'])
        shop_serializer = serializers.ShopSerializer(shop, many=True)

        current_offer['shop_name'] = shop_serializer.data[0]['name']
        current_offer['logo_link'] = shop_serializer.data[0]['logo_link']

        offers.append(current_offer)

    return Response(offers)

########################################################################


@api_view(['GET'])
def get_products_preview_search(request, product_name):

    products = models.Product.objects.filter(name__iexact=product_name)
    product_serializer = serializers.ProductSerializer(products, many=True)
    products = []
    for product in product_serializer.data:
        all_products_from_shops = models.ShopProduct.objects.filter(product_id=product['id'])
        shops_products_serializer = serializers.ShopProductSerializer(all_products_from_shops, many=True)
        max_price = -1
        min_price = math.inf
        for shops_product in shops_products_serializer.data:
            # print("price", shops_product['price'])
            if shops_product['price'] * shops_product['discount'] > max_price:
                max_price = shops_product['price'] * shops_product['discount']
            if shops_product['price'] * shops_product['discount'] < min_price:
                min_price = shops_product['price'] * shops_product['discount']

        current_product = product
        current_product['range'] = [str(min_price), str(max_price)]
        products.append(current_product)

    return Response(products)