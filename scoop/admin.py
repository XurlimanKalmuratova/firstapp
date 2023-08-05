from django.contrib import admin
from .models import Product, RepairProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price']
    list_filter = ['title']
    search_fields = ['title']


class RepairProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    list_filter = ['title']
    search_fields = ['title']


admin.site.register(RepairProduct, RepairProductAdmin)

