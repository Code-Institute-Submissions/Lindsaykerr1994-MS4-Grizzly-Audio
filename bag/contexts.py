from django.conf import settings
from django.shortcuts import get_object_or_404
from packs.models import Pack

def bag_contents(request):

    bag_items = []
    total = 0
    bag_count = 0
    bag = request.session.get('bag', {})

    for pack_id, quantity in bag.items():
        pack = get_object_or_404(Pack, pk=pack_id)
        total += pack.price
        bag_count = bag_count + 1
        bag_items.append({
            'pack_id': pack_id,
            'pack': pack,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'bag_count': bag_count,
    }
    return context
