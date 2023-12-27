from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import KTPmodel

class KTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = KTPmodel
        fields = ('id', 'img', 'img_path')
