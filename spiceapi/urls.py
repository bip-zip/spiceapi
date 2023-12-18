from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('orders.urls'))
]


admin.site.site_header = 'SpiceAPI'
admin.site.index_title = 'SpiceAPI'                   
admin.site.site_title = 'SpiceAPI Adminsitration'      