from django.db import models
from apps.products.models import Product
from apps.stores.models import Store

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, db_column='store_id')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    class Meta:
        db_table = 'price'
        unique_together = ('product', 'store', 'start_datetime')
