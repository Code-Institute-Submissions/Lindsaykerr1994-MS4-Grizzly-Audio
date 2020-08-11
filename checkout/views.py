from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your shopping bag right now")
        return redirect(reverse('packs'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H5Aq1Aweg9QeXppnZhu4gw4h8mdUJRECJuVopDccrF3MFo9GYpgX9HiW5tWbkXQPprs7NCUVWMQbUbUM4eAEf52003cgncuZ4',
        'client_secret_key': 'test secret key',
    }
    return render(request, template, context)
