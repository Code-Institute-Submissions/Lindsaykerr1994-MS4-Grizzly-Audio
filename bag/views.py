from django.shortcuts import render


def view_bag(request):
    """ Create a view to display and modify bag contents """
    return render(request, 'bag/bag.html')