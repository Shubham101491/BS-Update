from django.shortcuts import render
from bigstore import settings

# Model
from kitchen.models import Category1, Kitchen_base,popular1,popular2,popular3


def water_beverages(request):
    kitch = Kitchen_base.objects.all()
    p1 = popular1.objects.all()
    p2 = popular2.objects.all()
    p3 = popular3.objects.all()
    return render(request, 'kitchen/kitchen.html', {"BASE_URL": settings.BASE_URL,'kitch': kitch,'p1':p1,'p2':p2,'p3':p3})


def single(request):
    return render(request, 'other/single.html', {"BASE_URL": settings.BASE_URL})
