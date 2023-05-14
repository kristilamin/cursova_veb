# Register your models here.
from django.contrib import admin

from .models import Order, Product, Surovuna


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'wine_type', 'quantity_on_plant', 'created_at', 'price', 'price_for_all', 'surovuna_id')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'product_id', 'quantity_of_product', 'created_at', 'last_updated_at', 'order_status')


class SurovunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'surovuna_name', 'quantity_on_plant', 'vurobnucha_price_kg', 'vurobnucha_price_general_kg', 'delivery_price', 'delivery_name')


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Surovuna, SurovunaAdmin)