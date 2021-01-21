from django.shortcuts import render
from bigstore import settings

# Model
from kitchen.models import Category1, Kitchen_base, popular1, popular2, popular3
from home.models import Staples, Snacks, Fruits_Vegetables, Breakfast_Cereal


def carts(request):
    ids = list(request.session.get('cart').keys())
    kitch = Kitchen_base.objects.filter(id__in=ids)
    return render(request, 'other/order.html', {"BASE_URL": settings.BASE_URL, 'kitch': kitch})
