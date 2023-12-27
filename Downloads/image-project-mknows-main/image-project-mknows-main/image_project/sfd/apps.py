# sfd/apps.py

from django.apps import AppConfig
from django.conf import settings
from tensorflow.keras.models import load_model
import os

class ImageSimilarityAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sfd'

    def ready(self):
        # Load the pre-trained VGG16 model when the app is ready
        saved_model_path = os.path.join(settings.BASE_DIR, 'sfd', 'models', 'vgg16_model.h5')
        self.model = load_model(saved_model_path)

        # Disable training for all layers in the VGG16 model
        for model_layer in self.model.layers:
            model_layer.trainable = False