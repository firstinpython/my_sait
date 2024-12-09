from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Product(models.Model):
    name = models.CharField(verbose_name="name", max_length=120)
    description = models.TextField(verbose_name="description", max_length=300)
    price = models.PositiveIntegerField(verbose_name="price",
                                        validators=[MinValueValidator(100), MaxValueValidator(100000)])
    quantity = models.PositiveIntegerField(verbose_name="quantity", validators=[MinValueValidator(1)])
    image = models.FileField(verbose_name="image", upload_to="product_image")
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(to="Categories", on_delete=models.CASCADE)
    delivery_time = models.PositiveIntegerField(verbose_name="dlvtime")
    brand = models.ForeignKey(to="Brand", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.price} | {self.is_published}"


class Categories(models.Model):
    name = models.CharField(verbose_name="name", max_length=120)
    description = models.CharField(verbose_name="description", max_length=300)

    def __str__(self):
        return f"{self.name}"

class Brand(models.Model):
    name = models.CharField(verbose_name="brand_name", max_length=120)
    description = models.CharField(verbose_name="description", max_length=300)

    def __str__(self):
        return f"{self.name}"