from django.urls import path, include
from .views import RegistrationListCreate, RegistrationDetail

urlpatterns = [
    path('form/', RegistrationListCreate.as_view(), name='registration-list-create'),
    path('form/<int:pk>/', RegistrationDetail.as_view(), name='registration-detail'),
]