from rest_framework import serializers
from customer.serializers import CustomerSerializer
from product.serializers import ItemSerializer
from .models import OrderItem, Order

class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'item', 'quantity', 'discount', 'total_amount']

    def get_total_amount(self, obj):
        return obj.calculate_total_amount()

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    order_items = serializers.SerializerMethodField()

    def get_order_items(self, obj):
        items = obj.order_items.all()
        print(obj)
        print(items)
        return OrderItemSerializer(items, many=True).data


    class Meta:
        model = Order
        fields = ['id', 'ref_number', 'desc', 'entry_date', 'customer', 'order_items']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items', [])
        order = Order.objects.create(**validated_data)

        for order_item_data in order_items_data:
            OrderItem.objects.create(order=order, **order_item_data)

        return order
