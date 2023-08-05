from django import forms 
from .models import Product, RepairProduct


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class RepairProductForm(forms.ModelForm):
    class Meta:
        model = RepairProduct
        fields = ('title', 'image')

    
    

