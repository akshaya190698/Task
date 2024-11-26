from django.db import models
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    product_id = models.CharField(max_length=10, unique=True)
    available_stocks = models.IntegerField()
    price = models.FloatField()
    tax_percentage = models.FloatField()
    

    def __str__(self):
        return self.name


class Bill(models.Model):
    customer_email = models.EmailField()
    total_price_without_tax = models.FloatField()
    total_tax = models.FloatField()
    net_price = models.FloatField()
    paid_amount = models.FloatField()
    balance = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Bill for {self.customer_email} on {self.created_at}"


class BillItem(models.Model):
    bill = models.ForeignKey(Bill, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_price = models.FloatField()
    tax_amount = models.FloatField()
    total_price = models.FloatField()
    

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"