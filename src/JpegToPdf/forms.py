from django import forms

from .models import Jpeg

class JpegToPdfForm(forms.ModelForm):
    class Meta:
        model = Jpeg
        fields = ('file')
