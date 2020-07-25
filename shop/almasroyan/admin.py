from django.contrib import admin

from .models import Product, Product_Instance, Brand, Category
# Register your models here.


admin.site.register(Brand)
admin.site.register(Category)


class Product_InstanceInline(admin.TabularInline):
    model = Product_Instance
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','enable',)
    inlines = [Product_InstanceInline]

@admin.register(Product_Instance)
class Product_InstanceAdmin(admin.ModelAdmin):
    list_filter = ('Due_back',)

