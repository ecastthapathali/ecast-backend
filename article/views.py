from django.shortcuts import render
from .models import ArticleForm
from .serializer import ArticleFormSerializer
# import CREATE LIST UPDATE APIView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status


class ArticleListCreate(generics.ListCreateAPIView):
    queryset = ArticleForm.objects.all()
    serializer_class = ArticleFormSerializer
    
    def perform_create(self, serializer):
        try:
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            raise serializers.ValidationError(str(e))

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({
                'error': str(e),
                'status': f'{status.HTTP_400_BAD_REQUEST}'
            }, status=status.HTTP_400_BAD_REQUEST)
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArticleForm.objects.all()
    serializer_class = ArticleFormSerializer

    def perform_update(self, serializer):
        try:
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            raise serializers.ValidationError(str(e))