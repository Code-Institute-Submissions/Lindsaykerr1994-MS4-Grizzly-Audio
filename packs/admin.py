from django.contrib import admin
from .models import Pack, Category

# Register your models here.


class PackAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
        'publish_date',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Pack, PackAdmin)
admin.site.register(Category, CategoryAdmin)
