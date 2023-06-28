from django.shortcuts import render
from .models import IntakeForm
from django.http import HttpResponse

def home(request):

    intake = IntakeForm.objects.all()
    print(intake)
    return HttpResponse("Kamm Garyo")
