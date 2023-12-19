from rest_framework import serializers
from customer.serializers import CustomerSerializer
from product.serializers import ItemSerializer
from .models import OrderItem, Order
from product.models import Item

class OrderItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)  # the ItemSerializer for read-only operations
    item_id = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), source='item', write_only=True)
    amount = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'item', 'item_id', 'quantity', 'discount', 'amount']

    def get_amount(self, obj):
        return obj.calculate_item_total_amount()



class CreateOrderItemSerializer(serializers.ModelSerializer):
    item_id = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), source='item', write_only=True)
    amount = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'item_id', 'quantity', 'discount', 'amount']

    def get_amount(self, obj):
        return obj.calculate_item_total_amount()


    def create(self, validated_data):
        item_id = validated_data.get('item')
        try:
            item = Item.objects.get(pk=item_id.id)
            print(item)
        except Item.DoesNotExist:
            raise serializers.ValidationError("Item with specified ID does not exist.")
        
        validated_data.pop('item')
        order_item = OrderItem.objects.create(item=item, **validated_data)
        return order_item


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    order_items = serializers.SerializerMethodField()
    total_amount = serializers.SerializerMethodField()

    def get_total_amount(self, obj):
        return obj.calculate_total_amount()

    def get_order_items(self, obj):
        items = obj.order_items.all()
        print(obj)
        print(items)
        return OrderItemSerializer(items, many=True).data


    class Meta:
        model = Order
        fields = ['id', 'ref_number', 'desc', 'entry_date', 'total_amount', 'customer', 'order_items']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items', [])
        order = Order.objects.create(**validated_data)

        for order_item_data in order_items_data:
            OrderItem.objects.create(order=order, **order_item_data)

        return order


# to create objects in bulk 
class BulkOrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['ref_number', 'desc', 'entry_date', 'customer', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        OrderItem.objects.bulk_create([OrderItem(order=order, **item_data) for item_data in items_data])

        return order 