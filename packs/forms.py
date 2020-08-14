from django import forms
from .widgets import CustomClearableFileInput
from .models import Pack, Category


class PackForm(forms.ModelForm):
    class Meta:
        model = Pack
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        placeholders = {
            'name': 'Pack Name',
            'sku': 'SKU Number',
            'description': 'Pack Description',
            'price': 'Price',
            'reduced_price': 'Reduced Price',
            'on_sale': '',
            'category': 'Category',
            'image': 'Image',
        }
        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['category'].choices = friendly_names
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'pack-form-input'
            self.fields[field].label = False
