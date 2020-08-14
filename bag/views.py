from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from packs.models import Pack


def view_bag(request):
    """ Create a view to display and modify bag contents """
    return render(request, 'bag/bag.html')


def add_to_bag(request, pack_id):
    """ Allows user to add a pack to their shopping bag """
    pack = Pack.objects.get(pk=pack_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    if pack_id not in list(bag.keys()):
        bag[pack_id] = 1
        messages.success(request, f'Added {pack.name} to your shopping bag.')
    else:
        messages.error(request, f'{pack.name} is already in your shopping bag.')
    request.session['bag'] = bag
    return redirect(reverse('packs'))


def remove_from_bag(request, pack_id):
    """ Allows user to remove a pack from their shopping bag """
    try:
        pack = Pack.objects.get(pk=pack_id)
        bag = request.session.get('bag', {})
        bag.pop(pack_id)
        request.session['bag'] = bag
        messages.success(request, f'Removed {pack.name} from your shopping bag.')
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}.')
        return HttpResponse(status=500)
