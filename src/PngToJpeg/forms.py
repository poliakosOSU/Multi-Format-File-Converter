from django import forms

from .models import Png

class PngToJpegForm(forms.ModelForm):
    class Meta:
        model = Png
        fields = ('image_file',)
