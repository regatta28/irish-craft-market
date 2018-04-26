from django import forms
from .models import Product


class ProductPostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price')