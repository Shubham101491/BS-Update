from django.shortcuts import render
from bigstore import settings

from household.models import household,clean_accesory,popular1,popular2,popular3

def hold(request):
    house = clean_accesory.objects.all()
    p1 = popular1.objects.all()
    p2 = popular2.objects.all()
    p3 = popular3.objects.all()
    return render(request, 'household/hold.html', {"BASE_URL": settings.BASE_URL,'house':house,'p1':p1,'p2':p2,'p3':p3})
