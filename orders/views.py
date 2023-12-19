from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer, CreateOrderItemSerializer

# Generic view for listing and creating orders
class OrderListCreateGenericView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Generic view for retrieving, updating, and deleting a particular order
class OrderRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Generic view for listing and creating order items
class OrderItemListCreateGenericView(ListCreateAPIView):
    queryset = OrderItem.objects.all()
    def get_serializer_class(self):
        # Use OrderItemCreateSerializer for creating instances, OrderItemSerializer for other actions
        if self.request.method == 'POST':
            return CreateOrderItemSerializer
        return OrderItemSerializer


# Generic view for retrieving, updating, and deleting a particular order item
class OrderItemRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

