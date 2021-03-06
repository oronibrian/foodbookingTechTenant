from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'email', 'address', 'paid', 'created',
                    'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity',]
    list_filter = ['product', 'quantity', 'order']

admin.site.register(Order, OrderAdmin)

admin.site.register(OrderItem,OrderItemAdmin)
