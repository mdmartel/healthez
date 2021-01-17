from django import forms
import ..models

class barcodeForm(forms.ModelForm): 
  
    class Meta: 
        model = models.barcode
        fields = ['barcodeImage'] 