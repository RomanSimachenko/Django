from django.db import models


class Shop(models.Model):
    title = models.CharField("Title", max_length=400)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="images/shop")

    class Meta:
        db_table = "shop"
        verbose_name = "Shop"
        verbose_name_plural = "Shops"

    def __str__(self) -> str:
        return self.title


class CategoryDescription(models.Model):
    text = models.TextField("Description", max_length=1000)

    class Meta:
        db_table = "categorydescription"
        verbose_name = "CategoryDescription"
        verbose_name_plural = "CategoryDescriptions"

    def __str__(self) -> str:
        return self.text[:100]


class Category(models.Model):
    title = models.CharField("Title", max_length=200)
    description = models.ManyToManyField(
        CategoryDescription, verbose_name="Category description")

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField("Title", max_length=300)
    description = models.TextField("Description", max_length=1000)
    amount = models.PositiveIntegerField("Amount")
    price = models.FloatField("Price")
    active = models.BooleanField("Status")

    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, verbose_name="shop")
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ('-price',)
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Product image")
    image_path = models.ImageField("Image path", upload_to="images/product")

    class Meta:
        ordering = ('id',)
        db_table = "product_image"
        verbose_name = "ProductImage"
        verbose_name_plural = "ProductImages"

    def __str__(self) -> str:
        return self.product.title
