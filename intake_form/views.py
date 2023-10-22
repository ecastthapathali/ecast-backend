from django.shortcuts import render
from .models import IntakeForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import IntakeFormSerializer

@api_view(['GET', 'POST'])
def getData(request):
    intakeforms = IntakeForm.objects.all()
    serializer = IntakeFormSerializer(intakeforms, many=True)
    return Response(serializer.data)