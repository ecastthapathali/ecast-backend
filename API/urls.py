from django.urls import path
from . import views

urlpatterns = [
    path("", views.IntakeAPIView.as_view(), name='intake-view'), 
    path("create", views.IntakeListCreate.as_view(), name='intake-view-create'),
    path("update/<str:roll>", views.IntakeRetriveUpdateDestroy.as_view(), name="intake-retrive-update-destroy"),
    
]