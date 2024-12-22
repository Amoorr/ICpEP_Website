"""
forms.py is responsible for asking inputs from the users. 

"""


from django import forms
from .models import Product, Cart

class ProductForm(forms.ModelForm):
    """
    This is the form presented when the admins want to add products to the database
    """
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'tag', 'quantity']

class OrderForm(forms.ModelForm):
    """
    This is the form presented when the students want to order a specific product.
    """
    class Meta:
        model = Cart
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1}),
        }
        labels = {
            'quantity': 'Order Quantity',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 1:
            raise forms.ValidationError("Quantity must be at least 1.")
        return quantity
