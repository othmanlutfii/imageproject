# sfd/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageUploadSerializer
from .function import features

class Template(APIView):
    def post(self, request):
        return Response('It is a template', status=status.HTTP_200_OK)

class ImageSimilarityAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            nik = serializer.validated_data['nik']
            user_image = serializer.validated_data['image_1']

            try:
                result = features.process_image_similarity(nik, user_image)
                response_data = build_result(result)
                return Response(response_data, status=status.HTTP_200_OK)
            except ValueError as e:
                result = {'message': str(e)}
                response_data = build_result(result)
                return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        else:
            result = {'message': 'Invalid request data'}
            response_data = build_result(result)
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

def build_result(result):
    result = {
        "status": 200,
        "message": "success",
        "result": result
    }
    return result