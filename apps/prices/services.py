from datetime import datetime
from apps.prices.models import Price
from apps.promotions.models import Promotion

def get_final_price(product, store, date: datetime):
    price_qs = Price.objects.filter(
        product=product,
        stores=store,
        start_datetime__lte=date,
        end_datetime__gte=date
    )
    if not price_qs.exists():
        return None

    base_price = price_qs.first().value

    # Buscar todas las promociones activas
    promotions = Promotion.objects.filter(
        products=product,
        stores=store,
        start_datetime__lte=date,
        end_datetime__gte=date
    )

    if promotions.exists():
        best_discount = max([p.discount_percent for p in promotions])
        final_price = base_price * (1 - best_discount / 100)
    else:
        final_price = base_price

    return round(final_price, 2)
