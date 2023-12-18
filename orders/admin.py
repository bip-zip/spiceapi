from django.contrib import admin
from .models import Order, OrderItem

# for the tabular inline
class OrderItemsInline(admin.TabularInline):
    model= OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemsInline,] #to show related orderitems in the same page
    list_display = ('id', 'ref_number','customer')
    list_filter = ('entry_date',)
    
admin.site.register(Order, OrderAdmin)

