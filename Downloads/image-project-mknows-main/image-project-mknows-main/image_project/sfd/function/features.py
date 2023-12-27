# sfd/function/features.py

from PIL import Image
import numpy as np
import os
from tensorflow.keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from sklearn.metrics.pairwise import cosine_similarity
from django.apps import apps
from django.conf import settings

def load_image(image_path):
    input_image = Image.open(image_path)

    # Convert image to RGB (if not already in RGB mode)
    if input_image.mode != 'RGB':
        input_image = input_image.convert('RGB')

    resized_image = input_image.resize((224, 224))
    return resized_image

def get_image_embeddings(object_image):
    model = apps.get_app_config('sfd').model
    image_array = np.expand_dims(image.img_to_array(object_image), axis=0)
    # Preprocess the image array
    image_array = preprocess_input(image_array)
    image_embedding = model.predict(image_array)
    return image_embedding

def get_similarity_score(first_image_vector, second_image_vector):
    similarity_score = cosine_similarity(first_image_vector, second_image_vector).reshape(1,)
    return similarity_score[0]

def process_image_similarity(nik, user_image):
    supported_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    signature_image_path = None

    for ext in supported_extensions:
        potential_path = os.path.join(settings.BASE_DIR, 'sfd', 'main_signature', f'{nik}{ext}')
        if os.path.exists(potential_path):
            signature_image_path = potential_path
            break

    if signature_image_path:
        first_image = load_image(signature_image_path)
        second_image = load_image(user_image)
                
        first_image_vector = get_image_embeddings(first_image)
        second_image_vector = get_image_embeddings(second_image)

        similarity_score = get_similarity_score(first_image_vector, second_image_vector)

        if similarity_score > 0.8:
            result = {'message': 'Real signature detected', 'similarity_score': similarity_score}
        else:
            result = {'message': 'Potential forged image detected', 'similarity_score': similarity_score}

        return result
    else:
        raise ValueError('Signature image not found for the specified NIK')
