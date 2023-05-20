
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock/',include('inventory.urls')),
    path('suppliers/',include('transections.urls'))
]
