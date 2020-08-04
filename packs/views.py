from django.shortcuts import render, get_object_or_404
from .models import Pack


def all_packs(request):
    """ Show all audio packs, allow sorting and search queries """

    packs = Pack.objects.all()

    context = {
        'packs': packs,
    }

    return render(request, 'packs/packs.html', context)


def pack_detail(request, pack_id):
    """ Retrieves and displays a specific audio pack using its pack_id """

    pack = get_object_or_404(Pack, pk=pack_id)
    similar_packs = Pack.objects.all()

    context = {
        'pack': pack,
        'date_string': str(pack.publish_date)[6:8],
        'month_string': str(pack.publish_date)[4:6],
        'year_string': str(pack.publish_date)[0:4],
        'similar_packs': similar_packs
    }

    return render(request, 'packs/pack_detail.html', context)
