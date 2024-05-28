from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import IntakeFormViewSet

router = DefaultRouter()
router.register(r'intake', IntakeFormViewSet)

urlpatterns = [
    path('', include(router.urls)),
]