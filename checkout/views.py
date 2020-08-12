from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from packs.models import Pack
from bag.contexts import bag_contents
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'post_code': request.POST['post_code'],
            'county': request.POST['county'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, quantity in bag.items():
                try:
                    pack = Pack.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        pack=pack,
                    )
                    order_line_item.save()
                except Pack.DoesNotExist:
                    messages.error(request, ("There is an error with one of\
                        your items. Please contact us for further\
                            assistance!"))
                    order.delete()
                    return redirect(reverse('bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        else:
            messages.error(request, 'There is an error! Please confirm your\
                information and try again.')
            print(order_form.errors)
            return redirect(reverse('checkout'))
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There is nothing in your shopping bag\
                    right now")
            return redirect(reverse('packs'))

        current_bag = bag_contents(request)
        total = current_bag['total']
        """ This value must be an integer for Stripe's use """
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        order_form = OrderForm()
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """ This will confirm a successful order """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order({order_number}) was a success. A\
        confirmation email will be sent to your address.')
    if 'bag' in request.session:
        bag = request.session.get('bag', {})
        for item_id, quantity in bag.items():
            try:
                pack = Pack.objects.get(id=item_id)
                pack.sales += 1
                pack.save()
            except Pack.DoesNotExist:
                print("Didn't work")
        del request.session['bag']
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
