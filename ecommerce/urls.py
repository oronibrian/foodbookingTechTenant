
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from orders.views import OrderItemViewSet
from django.shortcuts import redirect

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'orders', OrderItemViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart', include('cart.urls')),
    path('orders/', include('orders.urls')),
    # path('', include('shop.urls')),
    path('api/v1/order/create', include('orders.api.urls')),
    path('api/',include(router.urls)),
    path('',lambda request:redirect('api/',permanent=False))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
