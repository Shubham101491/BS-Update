from django.shortcuts import render,redirect
from bigstore import settings

from personal_care.models import Personal,ayurvedic,popular1,popular2,popular3

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
    kitch = ayurvedic.objects.filter(id__in=ids)
    return redirect('care')

def care(request):
    ayurved = None
    ayurved = ayurvedic.objects.all()
    p1 = popular1.objects.all()
    p2 = popular2.objects.all()
    p3 = popular3.objects.all()
    data = {}
    data['BASE_URL'] = settings.BASE_URL
    data['ayurved'] = ayurved
    data['p1'] = p1
    data['p2'] = p2
    data['p3'] = p3
    return render(request, 'pcare/care.html', data)
