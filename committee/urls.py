from django.urls import path
from .views import CommitteeMemberListCreate,CommitteeMemberDetail

urlpatterns = [
    path('members/', CommitteeMemberListCreate.as_view(), name='committee-list'),
    path('members/<uuid:pk>/', CommitteeMemberDetail.as_view(), name='committee-detail'),
]
