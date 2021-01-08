from django.shortcuts import render
from bigstore import settings

from other.models import Offer, special_offer


def shipping(request):
    return render(request, 'other/shipping.html', {"BASE_URL": settings.BASE_URL})


def terms(request):
    return render(request, 'other/terms.html', {"BASE_URL": settings.BASE_URL})


def faqs(request):
    return render(request, 'other/faqs.html', {"BASE_URL": settings.BASE_URL})


def offer(request):
    offers = special_offer.objects.all()
    return render(request, 'other/offer.html', {"BASE_URL": settings.BASE_URL, 'offers': offers})


def wishlist(request):
    return render(request, 'other/wishlist.html', {"BASE_URL": settings.BASE_URL})


def single(request):
    return render(request, 'other/single.html', {"BASE_URL": settings.BASE_URL})
