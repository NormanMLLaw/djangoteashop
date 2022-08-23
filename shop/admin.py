from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('tea_name', 'tea_type', 'category', 'price', 'color', 'store','modified_date', 'is_available')
    prepopulated_fields = {'slug': ('tea_name'),}


admin.site.register(Product)