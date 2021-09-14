from django import forms
from .models import PixelCounter


class ImageForm(forms.ModelForm):
    class Meta:
        model = PixelCounter
        fields = ('title', 'cover')