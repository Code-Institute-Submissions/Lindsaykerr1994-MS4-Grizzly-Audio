from django.shortcuts import render
from packs.models import Pack

# Create your views here.


def index(request):
    """ A view to return the website's home page """
    best_sellers = Pack.objects.all()
    new_release = Pack.objects.all()
    free_packs = Pack.objects.all()

    context = {
        'best_sellers': best_sellers,
        'new_releases': new_release,
        'free_packs': free_packs,
    }
    return render(request, 'home/index.html', context)
