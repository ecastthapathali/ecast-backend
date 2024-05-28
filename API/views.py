from django.shortcuts import render
from  rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Intake
from .serializers import IntakeSerializer
# Create your views here.

class IntakeListCreate(generics.ListCreateAPIView):
    queryset = Intake.objects.all()
    serializer_class = IntakeSerializer

class IntakeRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Intake.objects.all()
    serializer_class = IntakeSerializer
    lookup_field = 'roll'

class IntakeAPIView(APIView):
    def get(self, request):
        queryset = Intake.objects.all()
        serializer = IntakeSerializer(queryset, many=True)
        return Response(serializer.data)
