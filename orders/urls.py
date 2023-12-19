from django.urls import path
from .views import OrderListCreateGenericView, OrderRetrieveUpdateDestroyGenericView, OrderItemRetrieveUpdateDestroyGenericView, OrderItemListCreateGenericView

app_name='orders'

urlpatterns = [
    path('', OrderListCreateGenericView.as_view(), name='order-list-create'),
    path('<int:pk>', OrderRetrieveUpdateDestroyGenericView.as_view(), name='order-retrieve-update-destroy'),

    # for orderitems
     path('orderitems', OrderItemListCreateGenericView.as_view(), name='orderitem-list-create'),
    path('orderitem/<int:pk>', OrderItemRetrieveUpdateDestroyGenericView.as_view(), name='orderitem-retrieve-update-destroy'),
]
