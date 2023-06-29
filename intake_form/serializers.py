from rest_framework import serializers
from intake_form.models import IntakeForm

class IntakeFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntakeForm
        fields = '__all__'