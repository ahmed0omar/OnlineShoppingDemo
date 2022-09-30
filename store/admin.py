from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 10
    search_fields = ['name']
