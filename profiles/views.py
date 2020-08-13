from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


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
    form = UserProfileForm(instance=profile)
    # Import user's order for order history
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile': True,
    }
    return render(request, template, context)
