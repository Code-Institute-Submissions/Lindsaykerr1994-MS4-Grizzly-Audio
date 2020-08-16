from django import forms
from .widgets import CustomClearableFileInput, CustomClearableImageInput
from .models import Pack, Category


class PackForm(forms.ModelForm):
    class Meta:
        model = Pack
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableImageInput)
    sample_track = forms.FileField(label='Sample Track', required=False,
                                   widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        # Adds placeholders and classes to form fields,
        # removes auto-generated labels and sets auto-focus
        # on the first field of the page
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Pack Name',
            'sku': 'SKU Number',
            'description': 'Description',
            'category': 'Category',
            'price': 'Price',
            'on_sale': 'On Sale?',
            'reduced_price': 'Reduced Price',
            'image': 'Image',
            'sample_track': 'Sample Track',
        }
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names
        self.fields['description'].widget.attrs['rows'] = '5'
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            if field != 'on_sale':
                self.fields[field].widget.attrs['class'] = \
                    'stripe-style-input w-100'
            self.fields[field].label = False
