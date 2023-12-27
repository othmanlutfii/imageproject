# sfd/models.py

from django.db import models

class ImageData(models.Model):
    nik = models.CharField(max_length=16, unique=True)
    image_path = models.CharField(max_length=255)

    def __str__(self):
        return self.nik
