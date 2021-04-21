from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/', include('delivery_backend.apps.delivery.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
