from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'product_id', 'available_stocks', 'price', 'tax_percentage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_id': forms.TextInput(attrs={'class': 'form-control'}),
            'available_stocks': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'tax_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
        }