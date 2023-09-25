from menu import products


def get_product_by_id(id):
    for product in products:
        if product['_id'] == id:
            return product
    return {}


def get_products_by_type(kind):
    product_type = []
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