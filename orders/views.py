from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

# Generic view for listing and creating orders
class OrderListCreateGenericView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Generic view for retrieving, updating, and deleting a particular order
class OrderRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Generic view for retrieving, updating, and deleting a particular order item
class OrderItemRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

