"""
Module: views.py

This module contains views for handling KTP OCR uploads.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import KTPSerializer
from .function import feature

class KTPOCRUpload(APIView):
    """
    API view for KTP OCR uploads.
    """

    def post(self, request):
        """
        Handle the POST request for KTP OCR uploads.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - Response: The HTTP response object.
        """
        try:
            serializer = KTPSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                result = feature.ktp_ocr(serializer.data['img_path'])
                return Response(build_result(result), status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

def build_result(result):
    """
    Build the result dictionary.

    Parameters:
    - result (dict): The result dictionary.

    Returns:
    - dict: The formatted result.
    """
    return {
        "status": 200,
        "message": "success",
        "result": result
    }
