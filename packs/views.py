from django.shortcuts import render
from .models import Pack


def all_packs(request):
    """ Show all audio packs, allow sorting and search queries """

    packs = Pack.objects.all()

    context = {
        'packs': packs,
    }

    return render(request, 'packs/packs.html', context)
