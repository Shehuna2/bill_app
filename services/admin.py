from django.contrib import admin
from .models import Service, Purchase

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'price')
    search_fields = ('name', 'service_type')
    list_filter = ('service_type',)

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'quantity', 'total_price', 'purchased_at')
    search_fields = ('user__username', 'service__name')
    list_filter = ('purchased_at',)
