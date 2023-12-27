from django.urls import path
from .views import Template
from .views import ImageSimilarityAPIView

urlpatterns = [
    path('template/', Template.as_view(), name='template_sfd'),
    path('image-similarity/', ImageSimilarityAPIView.as_view(), name='image_similarity'),
]
