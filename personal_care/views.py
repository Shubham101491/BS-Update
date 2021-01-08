from django.shortcuts import render
from bigstore import settings

from personal_care.models import Personal,ayurvedic,popular1,popular2,popular3

def care(request):
    ayurved = ayurvedic.objects.all()
    p1 = popular1.objects.all()
    p2 = popular2.objects.all()
    p3 = popular3.objects.all()
    return render(request, 'pcare/care.html', {"BASE_URL": settings.BASE_URL,'ayurved':ayurved,'p1':p1,'p2':p2,'p3':p3})