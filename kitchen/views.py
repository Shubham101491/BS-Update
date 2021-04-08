from django.shortcuts import render, redirect
from bigstore import settings

# Model
from kitchen.models import Category1, Kitchen_base, popular1, popular2, popular3
from home.models import Staples, Snacks, Fruits_Vegetables, Breakfast_Cereal


def product(request, id):
    product = request.POST.get('product')
    cart = request.session.get('cart')
    remove = request.POST.get('remove')
    if cart:
        quantity = cart.get(product)
        if quantity:
            if remove:
                if quantity <= 1:
                    cart.pop(product)
                else:
                    cart[product] = quantity-1
            else:
                cart[product] = quantity+1
        else:
            cart[product] = 1
    else:
        cart = {}
        cart[product] = 1
    request.session['cart'] = cart
    print('cart', request.session['cart'])
    ids = list(request.session.get('cart').keys())
    kitch = Kitchen_base.objects.filter(id__in=ids)
    return redirect('water_beverages')


def water_beverages(request):
    kitch = None
    kitch = Kitchen_base.objects.all()
    data = {}
    data['BASE_URL'] = settings.BASE_URL
    data['kitch'] = kitch
    print('you are :', request.session.get('username'))
    return render(request, 'kitchen/kitchen.html', data,)