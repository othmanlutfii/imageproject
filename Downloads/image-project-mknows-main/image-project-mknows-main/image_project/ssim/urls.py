from django.urls import path

from .views import Template, AnchorSignatureUpload, PredictSignatureSimilarity

urlpatterns = [
    path('template/', Template.as_view(), name='template_ssim'),
    path('upload-anchor/', AnchorSignatureUpload.as_view(), name='upload_anchor'),
    path('predict-similarity/', PredictSignatureSimilarity.as_view(), name='predict_similarity')
]
