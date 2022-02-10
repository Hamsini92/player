from rest_framework import serializers
from playerlistings.models import Intuit

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField

class SaveFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intuit
        fields = '__all__'