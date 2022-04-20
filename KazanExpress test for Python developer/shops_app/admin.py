from django.contrib import admin
from . import models


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image',)
    list_display_links = ('title',)
    search_fields = ('title',)
    readonly_fields = ('id',)


@admin.register(models.CategoryDescription)
class CategoryDescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text',)
    list_display_links = ('text',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'all_possible')
    list_display_links = ('title',)
    search_fields = ('id', 'title',)

    def all_possible(self, obj):
        from django.utils.html import format_html

        all_text = ""
        for o in obj.description.all():
            all_text += o.text[:100] + ";" + "<br>"
        return format_html(all_text)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'amount',
                    'price', 'active', 'shop',)
    list_display_links = ('title',)
    search_fields = ('id', 'title',)
    readonly_fields = ('id',)


@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image_path', 'image',)
    list_display_links = ('product',)

    def image(self, obj):
        from django.utils.html import format_html

        return format_html(f"""<img src="{obj.image_path.url}" style="max-width: 15%; max-heigth: 15%;">""")
