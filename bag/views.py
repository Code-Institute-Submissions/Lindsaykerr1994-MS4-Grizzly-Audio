from django.shortcuts import render, redirect


def view_bag(request):
    """ Create a view to display and modify bag contents """
    return render(request, 'bag/bag.html')


def add_to_bag(request, pack_id):
    """ Allows user to add a pack to their shopping bag """
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    if pack_id not in list(bag.keys()):
        bag[pack_id] = 1
    request.session['bag'] = bag
    return redirect(redirect_url)
