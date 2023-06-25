from django.contrib import admin
from .models import Countries, Shipment, Quotes

# Register your models here.

@admin.register(Countries)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_code', 'placement_point', 'current_location', 'destination', 'date_of_shipment')

@admin.register(Quotes)
class QuotesAdmin(admin.ModelAdmin):
    list_display = ('service', 'email', 'to_country', 'from_country')