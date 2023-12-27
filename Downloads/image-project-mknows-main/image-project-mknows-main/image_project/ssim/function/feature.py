"""

This module defines the SignatureClassifier class for predicting the authenticity of signatures.

"""

from keras.models import Model
from keras.applications import inception_v3
from keras.metrics import CosineSimilarity
import tensorflow as tf
from ..libraries import utils
from ..apps import SsimConfig

class SignatureClassifier(Model):
    """
    SignatureClassifier class extends Keras Model for signature authenticity prediction.

    Attributes:
    - embedding (tf.keras.Model): Siamese network embedding model.
    - threshold (float): Similarity threshold for classifying signatures.

    Methods:
    - __init__(self, siamese_embedding, threshold): Constructor method.
    - call(self, input_data): Abstract method for signature prediction.
    - predict(self, data, threshold=0.86): Predicts signature authenticity.
    - _compute_similarity(self, data): Computes cosine similarity between two signature images.
    - predict_similarity(self, serializer): Predicts authenticity using serialized input data.
    - preprocess_image(self, image_path): Preprocesses a signature image for model input.

    """

    def __init__(self, siamese_embedding, threshold):
        """
        Initialize the SignatureClassifier.

        Parameters:
        - siamese_embedding (tf.keras.Model): Siamese network embedding model.
        - threshold (float): Similarity threshold for classifying signatures.

        """

        super().__init__()
        self.embedding = siamese_embedding
        self.threshold = threshold

    def call(self, input_data):
        """
        Abstract method for signature prediction.

        Parameters:
        - input_data: Input data for the model.

        Returns:
        - Prediction result.

        """
        pass

    def predict(self, data, threshold=0.86):
        """
        Predicts signature authenticity.

        Parameters:
        - data: Tuple containing anchor and test signature images.
        - threshold (float): Similarity threshold for classification.

        Returns:
        - Dictionary containing 'is_fake' (boolean) and 'similarity_score' (float).

        """
        similarity_score = self._compute_similarity(data)
        is_fake = similarity_score < threshold

        return {'is_fake': is_fake.numpy(),
                'similarity_score': similarity_score.numpy()}

    def _compute_similarity(self, data):
        """
        Computes cosine similarity between anchor and test signature images.

        Parameters:
        - data: Tuple containing anchor and test signature images.

        Returns:
        - Cosine similarity score.

        """
        img_ori = data[0]
        img_test = data[1]

        img_ori_emb = self.embedding(inception_v3.preprocess_input(img_ori))
        img_test_emb = self.embedding(inception_v3.preprocess_input(img_test))

        cos_similarity = CosineSimilarity()
        similarity_score = cos_similarity(img_ori_emb, img_test_emb)

        return similarity_score

def predict_similarity(serializer):
    """
    Predicts authenticity using serialized input data.

    Parameters:
    - serializer: Serialized input data.

    Returns:
    - Prediction result.

    """
    nik = serializer.data.get('nik')
    anchor_path, test_path = utils.find_saved_signatures_by_nik(nik)
    anchor_image = preprocess_image(anchor_path)
    test_image = preprocess_image(test_path)

    data = (anchor_image, test_image)
    emb_model = SsimConfig.loaded_model
    model = SignatureClassifier(emb_model, 0.86)
    result = model.predict(data)

    utils.delete_signature_data_by_nik(nik)

    return result

def preprocess_image(image_path):
    """
    Preprocesses a signature image for model input.

    Parameters:
    - image_path: Path to the signature image.

    Returns:
    - Preprocessed image.

    """
    target_shape = (200, 200)
    image = tf.io.read_file(image_path)
    image = tf.image.decode_png(image, channels=3)
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.image.resize(image, target_shape)
    image = tf.expand_dims(image, axis=0)

    return image
