from django.shortcuts import render
from packs.models import Pack

# Create your views here.


def index(request):
    """ A view to return the website's home page """
    best_sellers = Pack.objects.order_by('-sales')[:5]
    new_release = Pack.objects.order_by('-publish_date')[:5]
    free_packs = Pack.objects.filter(price=0.00)[:5]

    context = {
        'best_sellers': best_sellers,
        'new_releases': new_release,
        'free_packs': free_packs,
    }
    return render(request, 'home/index.html', context)
