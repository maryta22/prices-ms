from rest_framework import viewsets
from .models import Store
from .serializers import StoreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.stores.models import Store
from apps.prices.models import Price

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

@api_view(['GET'])
def products_by_store(request):
    data = []
    stores = Store.objects.all()

    for store in stores:
        prices = Price.objects.filter(store=store).select_related('product')
        products = [
            {
                'id': price.product.id,
                'name': price.product.name,
                'price': float(price.value),
                'start_datetime': price.start_datetime.isoformat(),
                'end_datetime': price.end_datetime.isoformat()
            }
            for price in prices
        ]
        data.append({
            'store_id': store.id,
            'store_name': store.name,
            'products': products
        })

    return Response(data)