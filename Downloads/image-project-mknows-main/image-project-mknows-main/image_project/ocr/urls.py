from django.urls import path

from .views import KTPOCRUpload

urlpatterns = [
    # path('ktp_ocr/', KTPOCR.as_view(), name='KTPOCR'),
    path('ktp_ocr/', KTPOCRUpload.as_view(), name='KTPOCR'),
]
