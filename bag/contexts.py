def bag_content(request):

    bag_items = []
    total = 0
    bag_count = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'bag_count': bag_count,
    }
    return context
