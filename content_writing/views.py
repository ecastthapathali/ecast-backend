from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import ContentForm
from .serializers import ContentFormSerializer

@api_view(['GET', 'POST'])
def content_form_list(request):
    if request.method == 'GET':
        content_forms = ContentForm.objects.all()
        serializer = ContentFormSerializer(content_forms, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ContentFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def content_form_detail(request, id):
    try:
        content_form = ContentForm.objects.get(id=id)
    except ContentForm.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ContentFormSerializer(content_form)
        return Response(serializer.data)
