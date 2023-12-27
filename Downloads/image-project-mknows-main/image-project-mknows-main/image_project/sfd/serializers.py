# sfd/serializers.py

from rest_framework import serializers

class ImageUploadSerializer(serializers.Serializer):
    nik = serializers.CharField(max_length=255)
    image_1 = serializers.ImageField()
