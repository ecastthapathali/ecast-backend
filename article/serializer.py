from .models import ArticleForm
from rest_framework import serializers

class ArticleFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleForm
        fields = '__all__'
