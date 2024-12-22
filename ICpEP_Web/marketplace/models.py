"""
NOTES:

You must migrate the custom user models first before creating models in this 
application. After you migrated those custom user models and made authentications, you
must create a different tables linking their IDs to the products to avoid multiple table
creation upon migrations.



"""

from django.db import models
from accounts.models import CustomUser 
from django.conf import settings

class Product(models.Model):
    """
    Model for the product table
    """
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tag = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name

    def is_stock_available(self, order_quantity):
        return self.quantity >= order_quantity

    class Meta:
        db_table = 'Product'  # Specify the table name if you need to override Django's default behavior
        ordering = ['product_name']  # Example: Order the records by product name by default

class Cart(models.Model):
    """
    Model for the cart table
    """
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    order_status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Received', 'Received')],
        default='Pending'
    )
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Cart {self.cart_id} for {self.user}'

    def total_price(self):
        return self.quantity * self.product.price

    class Meta:
        db_table = 'Cart'  # Override table name if needed
        ordering = ['order_date']  # Order the records by order_date by default
