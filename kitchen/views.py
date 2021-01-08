from django.shortcuts import render
from bigstore import settings

# Model
from kitchen.models import Category1, Kitchen_base, popular1, popular2, popular3
from home.models import Staples,Snacks,Fruits_Vegetables,Breakfast_Cereal


def water_beverages(request):
    kitch = Kitchen_base.objects.all()
    p1 = popular1.objects.all()
    p2 = popular2.objects.all()
    p3 = popular3.objects.all()
    return render(request, 'kitchen/kitchen.html', {"BASE_URL": settings.BASE_URL, 'kitch': kitch, 'p1': p1, 'p2': p2, 'p3': p3})


# def kitch_prod(request,id):
#     hst = Staples.objects.all()
#     hsn = Snacks.objects.all()
#     fv = Fruits_Vegetables.objects.all()
#     bkf = Breakfast_Cereal.objects.all()
#     allimages = Kitchen_base.objects.filter(id=id)
#     return render(request, 'other/single.html', {"BASE_URL": settings.BASE_URL,'hst':hst,'hsn':hsn,'fv':fv,'bkf':bkf,'images': allimages})
