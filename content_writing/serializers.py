from rest_framework import serializers
from .models import ContentForm

class ContentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentForm
        fields = "__all__"
        
    