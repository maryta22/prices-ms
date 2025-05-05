from rest_framework import serializers

from apps.products.models import Product
from apps.stores.models import Store
from .models import Promotion, PromotionProductStore

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'

class PromotionProductStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionProductStore
        fields = '__all__'


class PromotionDetailSerializer(serializers.ModelSerializer):
    assignments = serializers.SerializerMethodField()

    class Meta:
        model = Promotion
        fields = [
            'id',
            'name',
            'discount_percent',
            'start_datetime',
            'end_datetime',
            'assignments'
        ]

    def get_assignments(self, obj):
        items = PromotionProductStore.objects.filter(promotion=obj).select_related('product', 'store')
        return [
            {
                'product': {'id': i.product.id, 'name': i.product.name},
                'store': {'id': i.store.id, 'name': i.store.name}
            }
            for i in items
        ]