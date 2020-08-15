from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        # Adds placeholders and classes to form fields,
        # removes auto-generated labels and sets auto-focus
        # on the first field of the page
        super().__init__(*args, **kwargs)
        self.fields['default_country'].widget.attrs['class'] = 'w-100 mt-0 mb-3 \
            rounded-0'
