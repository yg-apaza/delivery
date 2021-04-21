from django.urls import include, path
from rest_framework import routers
from delivery_backend.apps.delivery import views

router = routers.DefaultRouter()
router.register('queries', views.QueryResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
