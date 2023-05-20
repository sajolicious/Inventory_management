
from django.urls import path,include
from inventory.views import StockListView
my_viewset = StockListView.as_view({
    'get': 'list',
    'post': 'create',
    'delete':'destroy',
    'put': 'update',
    'patch': 'partial_update',
    })
urlpatterns = [
    path('<int:pk>/',my_viewset,name='inventory'),
  
]
