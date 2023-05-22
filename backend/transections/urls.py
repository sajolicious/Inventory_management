
from django.urls import path, include
from transections.views import SuppliersView, SuppliersCreateView, SupplierUpdateView, SupplierDelateView, SupplierProfileView, PurchaseCreateView
my_viewset = SuppliersView.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'destroy',
})
my_viewset1 = SuppliersCreateView.as_view({
    'post': 'create',
})
my_viewset2 = SupplierUpdateView.as_view({
    'get': 'list',
    'post': 'update',
})
my_viewset3 = SupplierDelateView.as_view({
    'delete': 'destroy',
})
SupplierProfileView = SupplierProfileView.as_view({
    'get': 'retrive',
})

PurchaseCreateView = PurchaseCreateView.as_view({

    'get': 'list',
    'post':'create'

})


urlpatterns = [
 
    path('<int:pk>/', my_viewset, name='inventory'),
    path('create/', my_viewset1, name='inventory'),
    path('update/<int:pk>/', my_viewset2, name='update'),
    path('delate/<int:pk>/', my_viewset3, name='delate'),
    path('SupplierProfileView/<int:pk>/', SupplierProfileView),
    path('purchases/new/', PurchaseCreateView,name='new-purchase'),
   

]
