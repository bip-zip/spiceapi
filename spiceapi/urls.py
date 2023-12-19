from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('api-schema', get_schema_view(title='SpiceAPI Schema', description="Guide for the REST API"), name='api_schema'),
    path('', TemplateView.as_view(template_name='docs.html',extra_context={'schema_url':'api_schema'})),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/customer/', include('customer.urls')),
    path('api/product/', include('product.urls')),
    path('api/order/', include('orders.urls'))
]


admin.site.site_header = 'SpiceAPI'
admin.site.index_title = 'SpiceAPI'                   
admin.site.site_title = 'SpiceAPI Adminsitration'      