from django.db import models
from django.conf import settings
import os

class KTPmodel(models.Model):
    img = models.ImageField(upload_to='images/', default=None)
    
    def img_path(self):
        return os.path.join(settings.MEDIA_ROOT, self.img.name)
    
    