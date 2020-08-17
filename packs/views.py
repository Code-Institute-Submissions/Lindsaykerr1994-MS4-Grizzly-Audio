from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Pack, Category
from .forms import PackForm


def all_packs(request):
    # Show all audio packs, allow sorting and search queries

    packs = Pack.objects.all()
    query = None
    sort = None
    direction = None
    categories = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                packs = packs.annotate(lower_name=Lower('name'))
                messages.info(request, 'Sorting by: Name')
            if sortkey == 'date':
                sortkey = 'publish_date'
                messages.info(request, 'Sorting by: Publication Date')
            if sortkey == 'category':
                sortkey = 'category__name'
                messages.info(request, 'Sorting by: Category')
            if sortkey == 'price':
                sortkey = 'price'
                messages.info(request, 'Sorting by: Price')
            if sortkey == 'freepacks':
                sortkey = 'lower_name'
                packs = packs.filter(price=0.00)
                packs = packs.annotate(lower_name=Lower('name'))
                messages.info(request, 'Sorting by: Free Packs')
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            else:
                direction = 'desc'
            packs = packs.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            packs = packs.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            for term in categories:
                category_term = term.friendly_name
            messages.info(request, f'You are searching for: {category_term}')

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.warning(request, "You did not enter any search\
                    criteria")
                return redirect(reverse('packs'))

            queries = Q(name__icontains=query) |\
                Q(description__icontains=query)
            messages.info(request, f'You are searching for: {queries}')
            packs = packs.filter(queries)
    edit_pack_form = PackForm()
    context = {
        'packs': packs,
        'search_term': query,
        'current_sorting': sort,
        'current_direction': direction,
        'current_categories': categories,
        'edit_pack_form': edit_pack_form,
    }

    return render(request, 'packs/packs.html', context)


@login_required
def add_pack(request):
    # Allows store owners to add a pack to the store
    # Check if user is a store owner
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = PackForm(request.POST, request.FILES)
        if form.is_valid():
            pack = form.save()
            messages.success(request, f'Successfully added new pack: \
                {pack.name}!')
            if 'id_saveandview' in request.POST:
                return redirect(reverse('packs'))
            else:
                return redirect(reverse('add_pack'))
        else:
            print(form.errors)
            messages.error(request, 'Failed to add pack. Please confirm\
            the information you entered, and try again.')
    else:
        form = PackForm()
    template = 'packs/add_pack.html'
    all_cat = Category.objects.all()
    context = {
        'form': form,
        'categories': all_cat,
    }
    return render(request, template, context)


@login_required
def edit_pack(request, pack_id):
    # Allow store owners to edit an existing pack
    # Check if user is a store owner
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page.')
        return redirect(reverse('home'))
    pack = get_object_or_404(Pack, pk=pack_id)
    if request.method == 'POST':
        form = PackForm(request.POST, request.FILES, instance=pack)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated pack: \
                {pack.name}!')
            return redirect(reverse('packs'))
        else:
            print(form.errors)
            messages.error(request, 'Failed to update pack. Please confirm\
            the information you entered, and try again.')
    else:
        form = PackForm(instance=pack)
        messages.info(request, f'You are editing {pack.name}')
    template = 'packs/edit_pack.html'
    all_cat = Category.objects.all()
    context = {
        'form': form,
        'pack': pack,
        'categories': all_cat,
    }
    return render(request, template, context)


@login_required
def delete_pack(request, pack_id):
    # Allows store owners to delete an existing product
    # Check if user is a store owner
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access to this page.')
        return redirect(reverse('home'))
    pack = get_object_or_404(Pack, pk=pack_id)
    pack.delete()
    messages.success(request, 'Pack has been successfully deleted!')
    return redirect(reverse('packs'))
