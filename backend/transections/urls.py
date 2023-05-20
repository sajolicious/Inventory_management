
from django.urls import path, include
from transections.views import SuppliersView, SuppliersCreateView, SupplierUpdateView, SupplierDelateView, SupplierProfileView, PurchaseBillView, UserLogin, PurchaseCreateView,PurchaseCreateVieww
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
PurchaseBill = PurchaseBillView.as_view({
    'get': 'retrive',
})

UserLogin = UserLogin.as_view({

    'post': 'login'

})
PurchaseCreateView = PurchaseCreateView.as_view({

    'get': 'list',
    'post':'create'

})
PurchaseCreateView1 = PurchaseCreateVieww.as_view({

    'get': 'list',
    'post':'create'

})
urlpatterns = [
    path('login/', UserLogin),
    path('<int:pk>/', my_viewset, name='inventory'),
    path('create/', my_viewset1, name='inventory'),
    path('update/<int:pk>/', my_viewset2, name='update'),
    path('delate/<int:pk>/', my_viewset3, name='delate'),
    path('SupplierProfileView/<int:pk>/', SupplierProfileView),
    path('PurchasebillView/<int:pk>/', PurchaseBill),

    path('purchases/new/', PurchaseCreateView,name='new-purchase'),
    path('purchases/ne/', PurchaseCreateView1,name='new-purchase'),

]
