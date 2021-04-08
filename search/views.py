from django.shortcuts import render
from bigstore import settings
from kitchen.models import Kitchen_base
from django.db.models import Q


def find(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')
        if query is not None:
            lookups = Q(item__icontains=query) | Q(detail__icontains=query)

            results = Kitchen_base.objects.filter(lookups).distinct()

            context = {'results': results, 'submitbutton': submitbutton}

            return render(request, 'search/search.html', context)

        else:
            return render(request, 'home/index.html')
    else:
        return render(request, 'home/index.html')
