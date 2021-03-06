from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_files = ('order_number', 'date', 'order_total',
                      'original_bag', 'stripe_pid')
    fields = ('full_name', 'user_profile', 'email', 'phone_number',
              'street_address1', 'street_address2',
              'town_or_city', 'county', 'post_code',
              'country', 'original_bag', 'stripe_pid')
    list_display = ('order_number', 'date', 'full_name', 'order_total')
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
