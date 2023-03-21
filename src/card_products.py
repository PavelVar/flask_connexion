import http.client

from flask import Response, abort, make_response
from iso4217 import Currency
from requests.status_codes import codes

CURRENCY_CODES = [elem for elem in Currency.__members__ if not elem.startswith("_")]


PRODUCTS = {
    'prod_1': {
        'name': 'PRODUCT_1',
        'currency': 'USD',
    },
    'prod_2': {
        'name': 'PRODUCT_2&',
        'currency': 'EUR',
    },
    'prod_3': {
        'name': 'PRODUCT_3?',
        'currency': 'LLL',
    },
}


def get_products() -> list[dict]:
    return [PRODUCTS[key] for key in sorted(PRODUCTS.keys())]


def create_product(product: dict) -> tuple:

    name = product.get('name')
    currency = product.get('currency', '')

    if not name or not currency:
        abort(codes.NOT_ACCEPTABLE, 'Empty name or currency')

    if name and name not in PRODUCTS:
        PRODUCTS[name] = {'name': name, 'currency': currency}
        return PRODUCTS[name], codes.CREATED

    abort(codes.NOT_ACCEPTABLE, f'Person with last name {name} already exists')


def get_one_product(name: str) -> dict:
    if name in PRODUCTS:
        return PRODUCTS[name]
    else:
        abort(codes.NOT_FOUND, f'Product {name} not found')


def update_product(name: str, product: dict) -> dict:
    if name in PRODUCTS:
        PRODUCTS[name]['currency'] = product.get("currency", product["currency"])
        PRODUCTS[name]['name'] = product.get('name', product['name'])
        return PRODUCTS[name]
    else:
        abort(codes.NOT_FOUND, f'Product {name} not found')


def delete_product(name: str) -> Response:
    if name in PRODUCTS:
        del PRODUCTS[name]
        return make_response(f'Product {name} successfully deleted', http.client.OK)
    abort(codes.NOT_FOUND, f'Product {name} not found')
