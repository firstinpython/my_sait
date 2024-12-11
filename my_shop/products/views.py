from django.core.paginator import Paginator
from .models import Product
from django.views.generic import ListView
from .filters import ProductFilter

# Create your views here.

class ProductListView(ListView):
    paginate_by = 2
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context