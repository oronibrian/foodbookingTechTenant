from django.urls import path
from.views import OrderCreateView,OrderRUDView
urlpatterns = [
    path('', OrderCreateView.as_view(),name='order-create'),
    path('<int:pk>', OrderRUDView.as_view(),name='order-rud'),


]