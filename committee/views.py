from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CommitteeMember, SocialMedia
from .serializers import CommitteeMemberSerializer, SocialMediaSerializer

class CommitteeMemberListCreate(generics.ListCreateAPIView):
    queryset = CommitteeMember.objects.all()
    serializer_class = CommitteeMemberSerializer
    print("CommitteeMemberListCreate called, Out from serializer_class:", serializer_class)
    def perform_create(self, serializer):
        serializer.save()
        print("CommitteeMemberListCreate perform_create called, Out from serializer:", serializer)
    

class CommitteeMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommitteeMember.objects.all()
    serializer_class = CommitteeMemberSerializer