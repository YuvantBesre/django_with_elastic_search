from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'created', 'modified')
    list_display_links = ['name']

admin.site.register(Product, ProductAdmin)
