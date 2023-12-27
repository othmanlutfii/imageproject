# sfd/forms.py
from django import forms

class ImageUploadForm(forms.Form):
    nik = forms.CharField(max_length=16, required=True)
    image_1 = forms.ImageField(required=True)