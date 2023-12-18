from django.contrib import admin
from orders.models import Order
from .models import Customer

# for the tabular inline
class OrderInline(admin.TabularInline):
    model= Order
    extra = 0

class CustomerAdmin(admin.ModelAdmin):
    inlines=[OrderInline,] #to show related orders in the same page
    list_display = ('name','email','contact')
    list_filter = ('created_on',)
    search_fields = ('name',)

admin.site.register(Customer, CustomerAdmin)
