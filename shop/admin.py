from django.contrib import admin

from shop.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    list_per_page = 4
    search_fields = ('title',)


admin.site.register(Product, ProductAdmin)


