from menu import products


def calculate_tab(menu):
    amount = 0
    for object in menu:
        for product in products:
            if product['_id'] == object['_id']:
                amount += product['price']*object['amount']        
    return {'subtotal': f'${round(amount, 2)}'}


def add_product(menu, **kwargs):
    new_id = 1

    if len(menu) > 0:
        new_id = max(product['_id'] for product in menu)+1

    new_product = {**kwargs, '_id': new_id}

    menu.append(new_product)
    return new_product