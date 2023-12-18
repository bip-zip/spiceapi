from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Order
from .serializers import OrderSerializer

# Generic view for listing and creating orders
class OrderListCreateGenericView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Generic view for retrieving, updating, and deleting a particular order
class OrderRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
