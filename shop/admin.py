from django.contrib import admin
from .models import Product, Variation

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('tea_name', 'tea_type', 'category', 'discounted_price', 'color', 'is_available')
    prepopulated_fields = {'slug': ('tea_name',)}
    

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable= ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
