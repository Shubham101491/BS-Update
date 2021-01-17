from django.shortcuts import render
from bigstore import settings


# Model
from home.models import Staples, Snacks, Fruits_Vegetables, Breakfast_Cereal
from kitchen.models import Category1, Kitchen_base, popular1, popular2, popular3
from personal_care.models import Personal, ayurvedic, popular1, popular2, popular3
from household.models import household, clean_accesory, popular1, popular2, popular3
from other.models import Offer, special_offer


def shipping(request):
    return render(request, 'other/shipping.html', {"BASE_URL": settings.BASE_URL})

def terms(request):
    return render(request, 'other/terms.html', {"BASE_URL": settings.BASE_URL})

def faqs(request):
    return render(request, 'other/faqs.html', {"BASE_URL": settings.BASE_URL})

def offer(request):
    hst = Staples.objects.all()
    hsn = Snacks.objects.all()
    fv = Fruits_Vegetables.objects.all()
    bkf = Breakfast_Cereal.objects.all()
    return render(request, 'other/offer.html', {"BASE_URL": settings.BASE_URL,
                                                'hst': hst, 'hsn': hsn, 'fv': fv, 'bkf': bkf})

def wishlist(request):
    return render(request, 'other/wishlist.html', {"BASE_URL": settings.BASE_URL})

# Kitchen Data
def single_detail_1(request, id):
    allimages = Kitchen_base.objects.filter(id=id)
    hst = Staples.objects.all()
    hsn = Snacks.objects.all()
    fv = Fruits_Vegetables.objects.all()
    bkf = Breakfast_Cereal.objects.all()
    return render(request, 'other/single.html', {"BASE_URL": settings.BASE_URL, 'images': allimages,
                                                 'hst': hst, 'hsn': hsn, 'fv': fv, 'bkf': bkf})

# Personal Data
def single_detail_2(request, id):
    allimages = ayurvedic.objects.filter(id=id)
    hst = Staples.objects.all()
    hsn = Snacks.objects.all()
    fv = Fruits_Vegetables.objects.all()
    bkf = Breakfast_Cereal.objects.all()
    return render(request, 'other/single.html', {"BASE_URL": settings.BASE_URL, 'images': allimages,
                                                 'hst': hst, 'hsn': hsn, 'fv': fv, 'bkf': bkf})

# HouseHold Data
def single_detail_3(request, id):
    allimages = clean_accesory.objects.filter(id=id)
    hst = Staples.objects.all()
    hsn = Snacks.objects.all()
    fv = Fruits_Vegetables.objects.all()
    bkf = Breakfast_Cereal.objects.all()
    return render(request, 'other/single.html', {"BASE_URL": settings.BASE_URL, 'images': allimages,
                                                 'hst': hst, 'hsn': hsn, 'fv': fv, 'bkf': bkf})

# Special Data
# def single_detail_4(request, id):
#     allimages = special_offer.objects.filter(id=id)
#     hst = Staples.objects.all()
#     hsn = Snacks.objects.all()
#     fv = Fruits_Vegetables.objects.all()
#     bkf = Breakfast_Cereal.objects.all()
#     return render(request, 'other/single.html', {"BASE_URL": settings.BASE_URL, 'images': allimages,
#                                                  'hst': hst, 'hsn': hsn, 'fv': fv, 'bkf': bkf})
