from django import forms

from .models import Jpeg

class JpegToPngForm(forms.ModelForm):
    class Meta:
        model = Jpeg
        fields = ('image_file',)
