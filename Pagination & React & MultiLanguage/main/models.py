from django.db import models


class Product(models.Model):
    title = models.CharField("Title", max_length=50)
    description = models.CharField("Description", max_length=1000)
    price = models.PositiveIntegerField(
        "Price", help_text="indicate price in USD($)")
    image = models.ImageField("Image")
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
