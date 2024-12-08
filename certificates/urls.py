from django.urls import path
from . import views  

urlpatterns = [
    path('generate-certificate/', views.generate_participation_certificate, name='generate_certificate'),
]
