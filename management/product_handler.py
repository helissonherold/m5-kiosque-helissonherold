from menu import products
from collections import Counter


def get_product_by_id(id):
    if type(id) != int:
        raise TypeError(f'product id must be an int')
    for product in products:
        if product['_id'] == id:
            return product
    return {}


def get_products_by_type(kind):
    product_type = []
    if type(kind) != str:
        raise TypeError(f'product type must be a str')
    for iten in products:
        if iten['type'] == kind:
            product_type.append(iten)

    return product_type


def add_product(menu, **kwargs):
    new_id = 1

    if len(menu) > 0:
        new_id = max(product['_id'] for product in menu)+1

    new_product = {**kwargs, '_id': new_id}

    menu.append(new_product)
    return new_product


def menu_report():
    product_count = len(products)
    total_prices = []
    total_types = []
    for product in products:
        total_prices.append(product['price'])
        total_types.append(product['type'])

    average_price = sum(total_prices)/product_count
    counter_types = Counter(total_types)
    common_type = counter_types.most_common(1)[0][0]

    return f'Products Count: {product_count} - Average Price: ${round(average_price, 2)} - Most Common Type: {common_type}'


def add_product_extra(menu, *required_keys, **product):
    new_id = 1
    product_keys = [*product]

    for key in required_keys:
        if key not in product_keys:
            raise KeyError(f'field {key} is required')

    for key in product_keys:
        if key not in required_keys:
            product.pop(key)

    if len(menu) > 0:
        new_id = max(product['_id'] for product in menu)+1
    else:
        new_id = 1

    product['_id'] = new_id

    menu.append(product)
    return product
