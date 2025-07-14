from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import ContactForm
from .serializers import ContactFormSerializer

class ContactFormListCreate(generics.ListCreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

    def perform_create(self, serializer):
        serializer.save()
        
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({
                'error': str(e),
                'status': status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)

class ContactFormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

    def perform_update(self, serializer):
        
        serializer.save()
