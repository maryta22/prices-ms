from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Promotion, PromotionProductStore
from .serializers import PromotionSerializer, PromotionDetailSerializer
from apps.products.models import Product
from apps.stores.models import Store

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PromotionDetailSerializer
        return PromotionSerializer

    @action(detail=True, methods=['patch'], url_path='assign')
    def assign_products_stores(self, request, pk=None):
        promotion = self.get_object()
        product_ids = request.data.get("product_ids", [])
        store_ids = request.data.get("store_ids", [])

        for product_id in product_ids:
            for store_id in store_ids:
                PromotionProductStore.objects.get_or_create(
                    promotion=promotion,
                    product_id=product_id,
                    store_id=store_id
                )

        return Response({"message": "Promocion asignada"}, status=status.HTTP_200_OK)
