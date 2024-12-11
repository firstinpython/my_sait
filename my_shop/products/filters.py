import django_filters
from .models import Product
from .widgets import CustomOrderingWidget

class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    price_order = django_filters.OrderingFilter(
        fields=(
            ('price', 'price'),
        ),
        widget=CustomOrderingWidget,
        label='Order'
    )

    class Meta:
        model = Product
        fields = ['price_min', 'price_max', 'price_order']