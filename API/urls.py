from django.urls import path
from . import views

urlpatterns = [
    path("", views.IntakeListCreate.as_view(), name='intake-view-create'),
    path("<str:roll>", views.IntakeRetriveUpdateDestroy.as_view(), name="update"),
]