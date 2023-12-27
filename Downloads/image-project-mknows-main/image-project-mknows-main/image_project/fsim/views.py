"""
Module for Django views using the REST framework.

This module includes views for rendering Django templates and 
handling API requests using the Django REST framework.
It also imports the necessary components for handling face-related 
tasks, including serializers and functions.

Imports:
    - `render` from `django.shortcuts`: A function for rendering Django templates.
    - `APIView` from `rest_framework.views`: A class for creating class-based views.
    - `Response` from `rest_framework.response`: A class for handling API responses.
    - `status` from `rest_framework`: Constants representing HTTP status codes.
    - `FaceSerializer` from `.serializers`: A serializer for face-related data.
    - `feature` from `.function`: A function for handling face-related tasks.

Example:
    >>> from django.shortcuts import render
    >>> from rest_framework.views import APIView
    >>> from rest_framework.response import Response
    >>> from rest_framework import status
    >>> from .serializers import FaceSerializer
    >>> from .function import feature

Note:
    Ensure that the required serializers and functions are defined and accessible.

See Also:
    - [Django documentation](https://docs.djangoproject.com/) for Django usage.
    - [Django REST framework documentation](https://www.django-rest-framework.org/) 
    for REST framework usage.
"""

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FaceSerializer
from .function import feature




class Template(APIView):
    """
    API endpoint for a template view.

    This class defines an API endpoint for handling HTTP POST requests.
    It returns a simple response indicating that it is a template.

    Methods:
        - post(request): Handles POST requests to the endpoint.

    Example:
        >>> # Make a POST request to the template view
        >>> response = Template().post(request_data)

    Note:
        - This is a template view and does not perform any specific functionality.
    """

    def post(self, request):
        """
        Handles HTTP POST requests to the template view.

        Parameters:
            request: The HTTP request object.

        Returns:
            Response: The HTTP response indicating that it is a template.

        Example:
            >>> response = Template().post(request_data)

        Note:
            - This is a template view and does not perform any specific functionality.
        """
        return Response('It is a template', status=status.HTTP_200_OK)


class AnchorFaceUpload(APIView):
    """
    API endpoint for uploading an anchor face.

    This class defines an API endpoint for handling HTTP POST requests to upload an anchor face.
    It updates the request data to indicate that it is an anchor face, 
    uses a serializer to validate and save the data,
    and returns a response with the result.

    Methods:
        - post(request, format=None): Handles POST requests to the endpoint.

    Example:
        >>> # Make a POST request to upload an anchor face
        >>> response = AnchorFaceUpload().post(request_data)

    Note:
        - The 'FaceSerializer' is used for validation and saving face data.
        - If successful, the response includes a status code, a success message, and the saved data.
        - If there are validation errors, the response includes a status code and error details.
    """

    def post(self, request, format=None):
        """
        Handles HTTP POST requests to upload an anchor face.

        Parameters:
            request: The HTTP request object.
            format: The requested format for the response.

        Returns:
            Response: The HTTP response indicating the result of the face upload.

        Example:
            >>> response = AnchorFaceUpload().post(request_data)

        Note:
            - The request data is updated to indicate that it is an anchor face.
            - If successful, the response includes a status code, 
            a success message, and the saved data.
            - If there are validation errors, the response includes a status code and error details.
        """
        try:
            request.data['is_anchor'] = True
            serializer = FaceSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(build_result(serializer.data), status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class PredictFaceSimilarity(APIView):
    """
    API endpoint for predicting face similarity.

    This class defines an API endpoint for handling HTTP POST requests to predict face similarity.
    It updates the request data to indicate that it is not an anchor face, 
    uses a serializer to validate and save the data,
    and returns a response with the predicted similarity result.

    Methods:
        - post(request, format=None): Handles POST requests to the endpoint.

    Example:
        >>> # Make a POST request to predict face similarity
        >>> response = PredictFaceSimilarity().post(request_data)

    Note:
        - The 'FaceSerializer' is used for validation and saving face data.
        - The 'feature.predict_similarity' function is used to predict face similarity.
        - If successful, the response includes a status code, 
        a success message, and the predicted similarity result.
        - If there are validation errors, the response includes a status code and error details.
    """

    def post(self, request, format=None):
        """
        Handles HTTP POST requests to predict face similarity.

        Parameters:
            request: The HTTP request object.
            format: The requested format for the response.

        Returns:
            Response: The HTTP response indicating the predicted face similarity result.

        Example:
            >>> response = PredictFaceSimilarity().post(request_data)

        Note:
            - The request data is updated to indicate that it is not an anchor face.
            - If successful, the response includes a status code, 
            a success message, and the predicted similarity result.
            - If there are validation errors, the response includes a status code and error details.
        """
        try:
            request.data['is_anchor'] = False
            serializer = FaceSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                result = feature.predict_similarity(serializer)
                result_final = {'Similarity': result[0], 'Is Similar?': result[1]}
                return Response(build_result(result_final), status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


def build_result(result):
    """
    Build a standardized result structure for API responses.

    Parameters:
        result: The result data to be included in the response.

    Returns:
        dict: A dictionary containing a standardized structure for API responses.

    Example:
        >>> result_data = {'example_key': 'example_value'}
        >>> response = build_result(result_data)

    Note:
        - The response structure includes a status code, a success message, and the actual result.
    """
    result = {
        "status": 200,
        "message": "success",
        "result": result
    }

    return result
