from django.contrib import admin
from .models import Order, OrderItem, Customer

# for the tabular inline
class OrderInline(admin.TabularInline):
    model= Order
    extra = 0

class CustomerAdmin(admin.ModelAdmin):
    inlines=[OrderInline,] #to show related orders in the same page
    list_display = ('name','email','contact')
    list_filter = ('created_on',)
    search_fields = ('name',)


# for the tabular inline
class OrderItemsInline(admin.TabularInline):
    model= OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemsInline,] #to show related orderitems in the same page
    list_display = ('id', 'ref_number','customer')
    list_filter = ('entry_date',)
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)

