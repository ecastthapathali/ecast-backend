from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.content_form_list, name='content-form-list'),
    path('form/<int:id>/', views.content_form_detail, name='content-form-detail'),
]
