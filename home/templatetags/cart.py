# video no - 37
from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(all, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == all.id:
            return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(all, cart):
    keys = cart.keys()
    for id in keys:
        # show error in id clear session no code changes
        if int(id) == all.id:
            return cart.get(id)
    return 0;


@register.filter(name='price_total')
def price_total(all, cart):
    print (all.discount_price * cart_quantity(all, cart))
    return all.discount_price * int(cart_quantity(all, cart))
    # ex return int(str(num) * 3)


@register.filter(name='total_price')
def total_price(all, cart):
    sum = 0
    for p in all:
        sum += price_total(p, cart)
    return sum
