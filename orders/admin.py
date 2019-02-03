from django.contrib import admin
from .models import *


class ProductsInOrderInline(admin.TabularInline):
    model = ProductsInOrder
    extra = 0


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields] #отобразить все поля


    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields] #отобразить все поля
    inlines = [ProductsInOrderInline]


    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductsInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductsInOrder._meta.fields] #отобразить все поля


    class Meta:
        model = ProductsInOrder


admin.site.register(ProductsInOrder, ProductsInOrderAdmin)


