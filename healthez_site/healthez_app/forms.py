from django import forms
from .models import barcode

class barcodeForm(forms.ModelForm): 
  
    class Meta: 
        model = barcode
        fields = ['barcode_Image'] 