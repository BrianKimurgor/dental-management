from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClinicViewSet

router = DefaultRouter()
router.register(r'', ClinicViewSet,)

urlpatterns = router.urls