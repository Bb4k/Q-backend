import requests

IP = '127.0.0.1:8000'


def insert_shops(API):
    url = 'http://' + IP + '/' + API

    shops = [
        {
            "name": "Auchan AFI",
            "latitude": 44.430306,
            "longitude": 26.052181,
            "logo_link": "https://i.ibb.co/Vtn8Cdz/auchan.png",
            "x_enter": 15,
            "y_enter": 16,
            "x_exit": 78,
            "y_exit": 16,
            "address": "Bulevardul General Paul Teodorescu 4, București 061344"
        },
        {
            "name": "Carrefour Orhideea",
            "latitude": 44.444576,
            "longitude": 26.063038,
            "logo_link": "https://i.ibb.co/jV9WRXh/carrefour.jpg",
            "x_enter": 15,
            "y_enter": 16,
            "x_exit": 78,
            "y_exit": 16,
            "address": "Splaiul Independenței 210, București 060025"
        },
        {
            "name": "Lidl Crangasi",
            "latitude": 44.451136,
            "longitude": 26.048280,
            "logo_link": "https://i.ibb.co/bKRjfXN/Lidl.png",
            "x_enter": 15,
            "y_enter": 16,
            "x_exit": 78,
            "y_exit": 16,
            "address": "Strada Sergent Ștefan Crișan 31, București 060311"
        },
        {
            "name": "Kaufland Militari",
            "latitude": 44.431506,
            "longitude": 26.006053,
            "logo_link": "https://i.ibb.co/1ndW4Qv/Kaufland.png",
            "x_enter": 15,
            "y_enter": 16,
            "x_exit": 78,
            "y_exit": 16,
            "address": "Strada Valea Cascadelor 3, București 061511"
        }
    ]

    for shop in shops:
        response = requests.post(url, json=shop)
        print(shop, response.status_code)


def insert_products(API):
    url = 'http://' + IP + '/' + API

    products = [
        {
            "name": "Chipsuri cu gust de smantana si ceapa",
            "category": "Dulciuri si snacks",
            "image_link": "https://d1lqpgkqcok0l.cloudfront.net/medias/sys_master/h08/h49/8945376690206.jpg?buildNumber=bdaaffa3e5c39b3dcb677db8d5f728cf1b32b791239ea193e3a23d4e394dfa73"
        },
        {
            "name": "Doritos cu gust de ardei iute",
            "category": "Dulciuri si snacks",
            "image_link": "https://d1lqpgkqcok0l.cloudfront.net/medias/sys_master/h83/h27/9146763608094.jpg?buildNumber=bdaaffa3e5c39b3dcb677db8d5f728cf1b32b791239ea193e3a23d4e394dfa73"
        },
        {
            "name": "Portocale",
            "category": "Legume si fructe",
            "image_link": "https://d1lqpgkqcok0l.cloudfront.net/medias/sys_master/h7f/h1f/9076333379614.jpg?buildNumber=bdaaffa3e5c39b3dcb677db8d5f728cf1b32b791239ea193e3a23d4e394dfa73"

        },
        {
            "name": "Granini de portocale",
            "category": "Suc",
            "image_link": "https://d1lqpgkqcok0l.cloudfront.net/medias/sys_master/h89/h75/9102269743134.jpg?buildNumber=bdaaffa3e5c39b3dcb677db8d5f728cf1b32b791239ea193e3a23d4e394dfa73"

        },
        {
            "name": "Almette",
            "category": "Lactate",
            "image_link": "https://d1lqpgkqcok0l.cloudfront.net/medias/sys_master/had/h85/9097487024158.jpg?buildNumber=bdaaffa3e5c39b3dcb677db8d5f728cf1b32b791239ea193e3a23d4e394dfa73"

        }

    ]

    for product in products:
        response = requests.post(url, json=product)
        print(product, response.status_code)


def insert_shopsproducts(API):
    url = 'http://' + IP + '/' + API

    shopsproducts = [
        {
            "product": 1,
            "shop": 1,
            "price": 5.4,
            "discount": 1.0,
            "x_coordinate": 30,
            "y_coordinate": 78,
        },
        {
            "product": 2,
            "shop": 1,
            "price": 5.2,
            "discount": 0.8,
            "x_coordinate": 70,
            "y_coordinate": 88,
        },
        {
            "product": 3,
            "shop": 1,
            "price": 6.3,
            "discount": 0.85,
            "x_coordinate": 86,
            "y_coordinate": 38,
        },
        {
            "product": 4,
            "shop": 1,
            "price": 9.6,
            "discount": 1.0,
            "x_coordinate": 110,
            "y_coordinate": 16,
        },
        {
            "product": 5,
            "shop": 1,
            "price": 4.3,
            "discount": 0.9,
            "x_coordinate": 78,
            "y_coordinate": 32,
        },
        {
            "product": 1,
            "shop": 2,
            "price": 5.7,
            "discount": 1.0,
            "x_coordinate": 30,
            "y_coordinate": 78,
        },
        {
            "product": 2,
            "shop": 2,
            "price": 7,
            "discount": 0.9,
            "x_coordinate": 70,
            "y_coordinate": 88,
        },
        {
            "product": 3,
            "shop": 2,
            "price": 9.4,
            "discount": 0.85,
            "x_coordinate": 86,
            "y_coordinate": 38,
        },
        {
            "product": 4,
            "shop": 2,
            "price": 13.7,
            "discount": 1.0,
            "x_coordinate": 110,
            "y_coordinate": 16,
        },
        {
            "product": 5,
            "shop": 2,
            "price": 7.5,
            "discount": 0.95,
            "x_coordinate": 78,
            "y_coordinate": 32,
        },
        {
            "product": 1,
            "shop": 3,
            "price": 8.5,
            "discount": 0.7,
            "x_coordinate": 30,
            "y_coordinate": 78,
        },
        {
            "product": 2,
            "shop": 3,
            "price": 12,
            "discount": 1.0,
            "x_coordinate": 70,
            "y_coordinate": 88,
        },
        {
            "product": 3,
            "shop": 3,
            "price": 12,
            "discount": 1.0,
            "x_coordinate": 86,
            "y_coordinate": 38,
        },
        {
            "product": 4,
            "shop": 3,
            "price": 14,
            "discount": 0.7,
            "x_coordinate": 110,
            "y_coordinate": 16,
        },
        {
            "product": 5,
            "shop": 3,
            "price": 7.8,
            "discount": 0.9,
            "x_coordinate": 78,
            "y_coordinate": 32,
        },
        {
            "product": 1,
            "shop": 4,
            "price": 9.3,
            "discount": 0.7,
            "x_coordinate": 30,
            "y_coordinate": 78,
        },
        {
            "product": 2,
            "shop": 4,
            "price": 10.0,
            "discount": 0.9,
            "x_coordinate": 70,
            "y_coordinate": 88,
        },
        {
            "product": 3,
            "shop": 4,
            "price": 9.5,
            "discount": 0.5,
            "x_coordinate": 86,
            "y_coordinate": 38,
        },
        {
            "product": 4,
            "shop": 4,
            "price": 7.6,
            "discount": 1.0,
            "x_coordinate": 110,
            "y_coordinate": 16,
        },
        {
            "product": 5,
            "shop": 4,
            "price": 5.8,
            "discount": 1.0,
            "x_coordinate": 78,
            "y_coordinate": 32,
        }

    ]

    for shopsproduct in shopsproducts:
        response = requests.post(url, json=shopsproduct)
        print(shopsproduct, response.status_code)


insert_shops("shop_create/")
insert_products("product_create/")
insert_shopsproducts("shopsproducts_create/")
