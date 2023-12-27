from pathlib import Path
import os

from django.apps import AppConfig
from paddleocr import PaddleOCR



class OcrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ocr'
    
    ocr_model = PaddleOCR(lang='en')
