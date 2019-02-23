from django.contrib import admin
from .models import Product, ProductImage
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title', 'description']
    list_display = ['title', 'thumbnail', 'price', 'active', 'updated']
    list_editable = ['price', 'active']
    list_filter = ['price', 'active']
    readonly_fields = ['updated', 'timestamp']
    prepopulated_fields = {'slug': ('title',)}
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'aaaffff', 'featured', 'updated']
    class Meta:
        model = ProductImage
admin.site.register(ProductImage, ProductImageAdmin)