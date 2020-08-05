from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Pack, Category


def all_packs(request):
    """ Show all audio packs, allow sorting and search queries """

    packs = Pack.objects.all()
    query = None
    sort = None
    direction = None
    categories = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == ' name':
                sortkey = 'lower_name'
                packs = packs.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            packs = packs.order_by(sortkey)   
  
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            packs = packs.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search criteria")
                return redirect(reverse('packs'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            packs = packs.filter(queries)


    current_sorting = f'{sort}_{direction}'

    context = {
        'packs': packs,
        'search_term': query, 
        'curent_sorting': current_sorting,
        'current_categories': categories,
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
