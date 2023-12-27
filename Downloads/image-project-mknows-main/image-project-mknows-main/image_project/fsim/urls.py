from django.urls import path

from .views import Template, AnchorFaceUpload, PredictFaceSimilarity

urlpatterns = [
    path('template/', Template.as_view(), name='template_fsim'),
    path('upload-anchor/', AnchorFaceUpload.as_view(), name='upload_anchor'),
    path('predict-similarity/', PredictFaceSimilarity.as_view(), name='predict_similarity')


]

