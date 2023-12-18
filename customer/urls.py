from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet

app_name='customer'

# for viewsets
router = DefaultRouter()
router.register(
'', CustomerViewSet, basename='customer'
    
)

urlpatterns = [
    path('', include(router.urls)),
]
