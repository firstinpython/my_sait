from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Product
from django.views import generic
from .filters import ProductFilter
from .forms import ProductCreateForm
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

class ProductListView(generic.ListView):
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


class CreateProductView(UserPassesTestMixin,generic.edit.FormView):
    model = Product
    template_name = 'products/create.html'
    form_class = ProductCreateForm
    success_url = reverse_lazy('product:product')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('product:product')  #    def test_func(self):






class UpdateProductView(UserPassesTestMixin,generic.UpdateView):
    model = Product
    fields = [
        "name",
        "description",
        "price",
        "quantity",
        "is_published",
        "category",
        "delivery_time",
        "brand"
    ]
    success_url = reverse_lazy('product:product')
    template_name = "products/update.html"

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('product:product')  #

class DeleteProductView(UserPassesTestMixin,generic.DeleteView):
    model = Product
    success_url = reverse_lazy('product:product')
    template_name = "products/delete.html"

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('product:product')  #

