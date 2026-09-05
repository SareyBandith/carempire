from django.contrib import admin
from .models import Brand, Car, Pro, Con


class ProInline(admin.TabularInline):
    model = Pro
    extra = 3


class ConInline(admin.TabularInline):
    model = Con
    extra = 3


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    search_fields = ['name']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'brand', 'year', 'price', 'fuel_type']
    list_filter = ['body_type', 'fuel_type', 'brand']
    search_fields = ['model_name']
    inlines = [ProInline, ConInline]


admin.site.register(Pro)
admin.site.register(Con)