from django.db import models
from apps.products.models import Product
from apps.stores.models import Store

class Promotion(models.Model):
    name = models.CharField(max_length=100, blank=True)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    class Meta:
        db_table = 'promotion'

class PromotionProductStore(models.Model):
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, db_column='promotion_id')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, db_column='store_id')

    class Meta:
        db_table = 'promotion_product_store'
