from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def profile(request):
    # A view to display the user's profile
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your information')
        else:
            messages.error(request, 'There was a problem updating your\
                information. Please check your information and try again.')
    # Import user's information from .forms
    else:
        form = UserProfileForm(instance=profile)
    # Import user's order for order history
    orders = profile.orders.all()
    for item in orders:
        print(item)
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile': True,
    }
    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is a past confirmation for order: {order_number}.'
        'A confirmation email was sent on the order date.'
    ))
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)
