from rest_framework import mixins, viewsets
from .models import Price
from .serializers import PriceSerializer
from rest_framework.decorators import api_view
from django.utils.dateparse import parse_datetime
from apps.products.models import Product
from apps.stores.models import Store
from apps.promotions.models import PromotionProductStore
from rest_framework.response import Response
from rest_framework import status


class PriceViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

@api_view(['POST'])
def create_price(request):
    ser = PriceSerializer(data=request.data)
    ser.is_valid(raise_exception=True)
    price = ser.save()
    return Response(PriceSerializer(price).data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def final_price(request):
    product_id = request.GET.get('product_id')
    store_id = request.GET.get('store_id')
    datetime_str = request.GET.get('datetime')

    if not all([product_id, store_id, datetime_str]):
        return Response({"error": "Parametros faltantes"}, status=400)

    date = parse_datetime(datetime_str)

    product = Product.objects.filter(id=product_id).first()
    store = Store.objects.filter(id=store_id).first()

    if not product or not store:
        return Response({"error": "Producto invalido"}, status=404)

    price_qs = Price.objects.filter(
        product=product,
        store=store,
        start_datetime__lte=date,
        end_datetime__gte=date
    )

    if not price_qs.exists():
        return Response({"error": "No existe precio para el producto en la tienda seleccionada"}, status=404)

    base_price = price_qs.first().value

    promotions = PromotionProductStore.objects.filter(
        product=product,
        store=store,
        promotion__start_datetime__lte=date,
        promotion__end_datetime__gte=date
    )

    if promotions.exists():
        best_discount = max([pps.promotion.discount_percent for pps in promotions])
        final_value = round(base_price * (1 - best_discount / 100), 2)
    else:
        final_value = base_price

    return Response({
        "product": product.name,
        "store": store.name,
        "base_price": base_price,
        "final_price": final_value,
        "applied_discount": float(best_discount) if promotions else 0.0
    })