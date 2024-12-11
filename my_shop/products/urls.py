from django.urls import path
from .views import  ProductListView,CreateProductView, UpdateProductView, DeleteProductView

app_name = "product"
urlpatterns = [
    path("",ProductListView.as_view(),name="product"),
    path('create_product', CreateProductView.as_view()),
    path('update/<pk>', UpdateProductView.as_view()),
    path('delete/<pk>',DeleteProductView.as_view())
]