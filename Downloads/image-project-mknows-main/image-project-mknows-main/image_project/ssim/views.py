"""
Module: views.py
----------------

This module defines Django REST framework views for handling signature-related functionality.

"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignatureSerializer
from .function import feature

class Template(APIView):
    """
    Template class for a simple API view.

    Methods:
    - post(self, request): Handles POST requests and returns a template response.

    """

    def post(self, request):
        """
        Handles POST requests and returns a template response.

        Parameters:
        - request: Django REST framework request object.

        Returns:
        - Response: A Response object with a message indicating it is a template.

        """
        return Response('It is a template', status=status.HTTP_200_OK)

class AnchorSignatureUpload(APIView):
    """
    APIView class for uploading anchor signature images.

    Methods:
    - post(self, request): Handles POST requests for uploading anchor signature images.

    """

    def post(self, request):
        """
        Handles POST requests for uploading anchor signature images.

        Parameters:
        - request: Django REST framework request object.

        Returns:
        - Response: A Response object with the result of the anchor signature upload.

        """
        try:
            request.data['is_anchor'] = True
            serializer = SignatureSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(build_result(serializer.data), status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

class PredictSignatureSimilarity(APIView):
    """
    APIView class for predicting signature similarity.

    Methods:
    - post(self, request): Handles POST requests for predicting signature similarity.

    """

    def post(self, request):
        """
        Handles POST requests for predicting signature similarity.

        Parameters:
        - request: Django REST framework request object.

        Returns:
        - Response: A Response object with the result of the signature similarity prediction.

        """
        try:
            request.data['is_anchor'] = False
            serializer = SignatureSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                result = feature.predict_similarity(serializer)
                return Response(build_result(result), status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

def build_result(result):
    """
    Builds a standardized result dictionary.

    Parameters:
    - result: The result data to include in the dictionary.

    Returns:
    - dict: A dictionary containing status, message, and result.

    """
    result = {
        "status": 200,
        "message": "success",
        "result": result
    }

    return result
