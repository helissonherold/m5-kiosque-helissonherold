from menu import products


def calculate_tab(menu):
    amount = 0 
    for object in menu:
        for product in products:
            if product['_id'] == object['_id']:
                amount += product['price']*object['amount']               
    return {'subtotal': f'${round(amount, 2)}'}
