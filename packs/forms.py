from django import forms
from .widgets import CustomClearableFileInput
from .models import Pack


class PackForm(forms.ModelForm):
    class Meta:
        model = Pack
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = 'w-100 mt-0 mb-3 \
            rounded-0'
        self.fields['description'].widget.attrs['rows'] = '5'
