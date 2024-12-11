from django.contrib import admin
from .models import Product,Category,Brand
from django_mptt_admin.admin import DjangoMpttAdmin
# Register your models here.

admin.site.register(Product)
admin.site.register(Brand)

@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {'slug':('title',)}