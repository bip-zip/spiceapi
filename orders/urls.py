from django.urls import path
from .views import OrderListCreateGenericView, OrderRetrieveUpdateDestroyGenericView

app_name='orders'

urlpatterns = [
    path('', OrderListCreateGenericView.as_view(), name='order-list-create'),
    path('<int:pk>', OrderRetrieveUpdateDestroyGenericView.as_view(), name='order-retrieve-update-destroy'),
]
