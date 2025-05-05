# apps/prices/serializers.py
from rest_framework import serializers
from .models import Price

class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = '__all__'

    def validate(self, data):
        product = data['product']
        store   = data['store']
        start   = data['start_datetime']
        end     = data['end_datetime']

        qs = Price.objects.filter(
            product=product,
            store=store,
            start_datetime__lt=end,
            end_datetime__gt=start,
        )
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            conflict = qs.first()
            serialized = PriceSerializer(conflict).data
            raise serializers.ValidationError({
                "detail": "El rango solicitado se solapa con un precio existente.",
                "conflict": serialized
            })

        return data
