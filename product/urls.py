from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

app_name='product'

# for viewsets
router = DefaultRouter()
router.register(
'', ItemViewSet, basename='item'
    
)

urlpatterns = [
    path('', include(router.urls)),
]
