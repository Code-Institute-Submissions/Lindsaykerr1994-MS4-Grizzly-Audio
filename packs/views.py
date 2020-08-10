from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
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
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            packs = packs.order_by(sortkey)
            messages.info(request, f'You are sorting by: {sortkey.capitalize()}')

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            for term in categories:
                category_term = term.capitalize()
            messages.info(request, f'You are searching for: {category_term}')
            packs = packs.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.warning(request, "You did not enter any search criteria")
                return redirect(reverse('packs'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            messages.info(request, f'You are searching for: {queries}')
            packs = packs.filter(queries)

    context = {
        'packs': packs,
        'search_term': query,
        'current_sorting': sort,
        'current_direction': direction,
        'current_categories': categories,
    }

    return render(request, 'packs/packs.html', context)


def pack_detail(request, pack_id):
    """ Retrieves and displays a specific audio pack using its pack_id """

    pack = get_object_or_404(Pack, pk=pack_id)
    category = pack.category.pk
    packs = Pack.objects.all()
    similar_packs = packs.filter(category=category)
    for this_pack in similar_packs:
        if this_pack == pack:
            similar_packs = similar_packs.exclude(pk=this_pack.id)
    similar_packs = similar_packs[:2]

    context = {
        'pack': pack,
        'date_string': str(pack.publish_date)[6:8],
        'month_string': str(pack.publish_date)[4:6],
        'year_string': str(pack.publish_date)[0:4],
        'similar_packs': similar_packs
    }

    return render(request, 'packs/pack_detail.html', context)
