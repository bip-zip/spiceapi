from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name','uom','rate')
    list_filter = ('item_name',)
    search_fields = ('item_name',)

admin.site.register(Item, ItemAdmin)