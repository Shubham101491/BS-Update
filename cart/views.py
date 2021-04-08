from django.shortcuts import render, redirect
from bigstore import settings

# Model
from kitchen.models import Category1, Kitchen_base, popular1, popular2, popular3
from personal_care.models import Personal, ayurvedic, popular1, popular2, popular3
from cart.models import Order
# form
from cart.forms import CheckoutForm


def order(request):
    ids = list(request.session.get('cart').keys())
    product = Kitchen_base.objects.filter(id__in=ids)
    # product = ayurvedic.objects.filter(id__in=ids)
    return render(request, 'cart/order2.html', {"BASE_URL": settings.BASE_URL, 'product': product})


def checkout(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        checkout = CheckoutForm(request.POST)
        cart = request.session.get('cart')
        ids = list(request.session.get('cart').keys())
        product = Kitchen_base.objects.filter(id__in=ids)
        print(user, checkout, cart, ids, product)

        # video continue 9 min
        # for p in product:
        #     order = 
        return redirect('home')
    else:
        checkout = CheckoutForm()
    return render(request, 'cart/checkout.html', {"BASE_URL": settings.BASE_URL, 'checkout_form': checkout})


# def checkout(request):
#     if request.method == 'POST':
#         checkout = CheckoutForm(request.POST)
#         if checkout.is_valid():
#             checkout.save()
#             return redirect('checkout')
#     else:
#         checkout = CheckoutForm()
#     return render(request, 'cart/checkout.html', {"BASE_URL": settings.BASE_URL, 'checkout_form': checkout})