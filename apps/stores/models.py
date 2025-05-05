from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'store'
