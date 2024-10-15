from django.urls import path
from . import views

urlpatterns = [
    path('shops/', views.get_shops),
    path('products/', views.get_products),
    path('shopsproducts/', views.get_shops_products),

    path('shop_create/', views.post_shop),
    path('product_create/', views.post_product),
    path('shopsproducts_create/', views.post_shops_product),

    path('get_products_preview/', views.get_products_preview),
    path('shop/<int:shop_id>/product/<int:product_id>/', views.get_product_from_shop),
    path('get_basket_prices/', views.get_basket_prices),
    path('get_shop_map/<int:shop_id>', views.get_map),
    path('get_offers/', views.get_offers),
    path('get_products_preview_search/<str:product_name>', views.get_products_preview_search),


]
