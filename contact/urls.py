from django.urls import path
from .views import ContactFormListCreate, ContactFormDetail

urlpatterns = [
    path('form/', ContactFormListCreate.as_view(), name='contactform-list-create'),
    path('form/<uuid:pk>/', ContactFormDetail.as_view(), name='contactform-detail'),
]
