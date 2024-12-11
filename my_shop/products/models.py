from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Product(models.Model):
    name = models.CharField(verbose_name="name", max_length=120)
    description = models.TextField(verbose_name="description", max_length=300)
    price = models.PositiveIntegerField(verbose_name="price",
                                        validators=[MinValueValidator(100), MaxValueValidator(100000)])
    quantity = models.PositiveIntegerField(verbose_name="quantity", validators=[MinValueValidator(1)])
    image = models.FileField(verbose_name="image", upload_to="product_image",null=True)
    is_published = models.BooleanField(default=True)
    category = TreeForeignKey('Category', on_delete=models.CASCADE)
    delivery_time = models.PositiveIntegerField(verbose_name="dlvtime")
    brand = models.ForeignKey(to="Brand", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.price} | {self.is_published}"

class Category(MPTTModel):
    title = models.CharField(max_length=255, verbose_name="Название категории")
    slug = models.SlugField(max_length=255, verbose_name="URL категории")
    description = models.TextField(verbose_name='Описание категории', max_length=300)
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank= True,
                            db_index=True,
                            related_name='children',
                            verbose_name="Родительская категория")

    class MPTTMeta:
        order_insertion_by = ('title',)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"{self.title}"


class Brand(models.Model):
    name = models.CharField(verbose_name="brand_name", max_length=120)
    description = models.CharField(verbose_name="description", max_length=300)

    def __str__(self):
        return f"{self.name}"